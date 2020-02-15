from prompto.param.ITypedParameter import ITypedParameter
from prompto.param.UnresolvedParameter import UnresolvedParameter
from prompto.error.SyntaxError import SyntaxError
from prompto.expression.ValueExpression import ValueExpression
from prompto.expression.MethodSelector import MethodSelector
from prompto.grammar.Argument import Argument
from prompto.grammar.ArgumentList import ArgumentList
from prompto.literal.DictLiteral import DictLiteral
from prompto.runtime.Context import MethodDeclarationMap
from prompto.statement.MethodCall import MethodCall
from prompto.type.DictType import DictType
from prompto.type.TextType import TextType
from prompto.utils import CmdLineParser
from prompto.value.DictValue import DictValue
from prompto.value.TextValue import TextValue


class Interpreter(object):
    argsType = DictType(TextType.instance)

    @staticmethod
    def interpretTests(context):
        for test in context.tests.values():
            local = context.newLocalContext()
            test.interpret(local)

    @staticmethod
    def interpretTest(context, name):
        test = context.tests[name]
        local = context.newLocalContext()
        test.interpret(local)

    @staticmethod
    def interpretMainNoArgs(context):
        Interpreter.interpret(context, "main", "")


    @staticmethod
    def interpret(context, methodName, cmdLineArgs):
        try:
            method = Interpreter.locateMethod(context, methodName, cmdLineArgs)
            arguments = Interpreter.buildArguments(method, cmdLineArgs)
            call = MethodCall(MethodSelector(methodName), arguments)
            call.interpret(context)
        finally:
            context.terminated()


    @staticmethod
    def buildArguments(method, cmdLineArgs):
        arguments = ArgumentList()
        if len(method.getArguments()) == 1:
            name = method.getArguments()[0].getName()
            value = Interpreter.parseCmdLineArgs(cmdLineArgs)
            arguments.append(Argument(UnresolvedParameter(name), value))
        return arguments


    @staticmethod
    def parseCmdLineArgs(cmdLineArgs):
        try:
            args = CmdLineParser.parseCmdLine(cmdLineArgs)
            valueArgs = dict()
            for key, value in args:
                valueArgs[TextValue(key)] = TextValue(value)
            dict_ = DictValue(TextType.instance, False, value=valueArgs)
            return ValueExpression(Interpreter.argsType, dict_)
        except:
            # TODO
            return DictLiteral(False)


    @staticmethod
    def locateMethod(context, methodName, cmdLineArgs):
        map = context.getRegisteredDeclaration(MethodDeclarationMap, methodName)
        if map is None:
            raise SyntaxError("Could not find a \"" + methodName + "\" method.")
        return Interpreter.locateMethodInMap(map, cmdLineArgs)


    @staticmethod
    def locateMethodInMap(map, cmdLineArgs):
        if cmdLineArgs is None:
            return Interpreter.locateMethodWithTypes(map)
        else:
            return Interpreter.locateMethodWithTypes(map, [DictType(TextType.instance)])


    @staticmethod
    def locateMethodWithTypes(methodMap, argTypes=None):
        if not argTypes:
            argTypes = []
        # try exact match first
        for method in methodMap.values():
            if Interpreter.identicalArguments(method.getArguments(), argTypes):
                return method
        # match Text{} argument, will pass None
        if len(argTypes) == 0:
            for method in methodMap.values():
                if Interpreter.isSingleTextDictArgument(method.getArguments()):
                    return method
        # match no argument, will ignore options
        for method in methodMap.values():
            if len(method.getArguments()) == 0:
                return method
        raise SyntaxError("Could not find a compatible \"" + methodMap.getName() + "\" method.")


    @staticmethod
    def isSingleTextDictArgument(arguments):
        if len(arguments) != 1:
            return False
        arg = arguments[0]
        if not isinstance(arg, ITypedParameter):
            return False
        return arg.getType() == Interpreter.argsType


    @staticmethod


    def identicalArguments(arguments, argTypes):
        if len(arguments) != len(argTypes):
            return False
        idx = 0
        for argument in arguments:
            if not isinstance(argument, ITypedParameter):
                return False
            argType = argTypes[idx]
            idx += 1
            if argType != argument.getType():
                return False
        return True
