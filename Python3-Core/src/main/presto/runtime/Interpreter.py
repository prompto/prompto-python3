from presto.type.DictType import DictType
from presto.type.TextType import TextType
from presto.statement.MethodCall import MethodCall
from presto.expression.MethodSelector import MethodSelector
from presto.grammar.ArgumentAssignmentList import ArgumentAssignmentList
from presto.grammar.ArgumentAssignment import ArgumentAssignment
from presto.grammar.UnresolvedArgument import UnresolvedArgument
from presto.utils.ArgsParser import ArgsParser
from presto.value.Text import Text
from presto.value.Dictionary import Dictionary
from presto.literal.DictLiteral import DictLiteral
from presto.value.ExpressionValue import ExpressionValue
from presto.runtime.Context import MethodDeclarationMap
from presto.grammar.ITypedArgument import ITypedArgument
from presto.error.SyntaxError import SyntaxError

class Interpreter(object):
    argsType = DictType(TextType.instance)

    @staticmethod
    def interpretMainNoArgs(context):
        Interpreter.interpret(context, "main", "")


    @staticmethod
    def interpret(context, methodName, cmdLineArgs):
        try:
            method = Interpreter.locateMethod(context, methodName, cmdLineArgs)
            assignments = Interpreter.buildAssignments(method, cmdLineArgs)
            call = MethodCall(MethodSelector(methodName), assignments)
            call.interpret(context)
        finally:
            context.terminated()


    @staticmethod
    def buildAssignments(method, cmdLineArgs):
        assignments = ArgumentAssignmentList()
        if len(method.getArguments()) == 1:
            name = method.getArguments()[0].getName()
            value = Interpreter.parseCmdLineArgs(cmdLineArgs)
            assignments.append(ArgumentAssignment(UnresolvedArgument(name), value))
        return assignments


    @staticmethod
    def parseCmdLineArgs(cmdLineArgs):
        try:
            args = ArgsParser.parse(cmdLineArgs)
            valueArgs = dict()
            for key, value in args:
                valueArgs[Text(key)] = Text(value)
            dict = Dictionary(valueArgs)
            return ValueExpression(Interpreter.argsType, dict)
        except:
            # TODO
            return DictLiteral()


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
    def locateMethodWithTypes(map, argTypes=[]):
        # try exact match first
        for method in map.values():
            if Interpreter.identicalArguments(method.getArguments(), argTypes):
                return method
        # match Text{} argument, will pass None
        if len(argTypes) == 0:
            for method in map.values():
                if Interpreter.isSingleTextDictArgument(method.getArguments()):
                    return method
        # match no argument, will ignore options
        for method in map.values():
            if len(method.getArguments()) == 0:
                return method
        raise SyntaxError("Could not find a compatible \"" + map.getName() + "\" method.")


    @staticmethod
    def isSingleTextDictArgument(arguments):
        if len(arguments) != 1:
            return False
        arg = arguments[0]
        if not isinstance(arg, ITypedArgument):
            return False
        return arg.getType() == Interpreter.argsType


    @staticmethod


    def identicalArguments(arguments, argTypes):
        if len(arguments) != len(argTypes):
            return False
        idx = 0
        for argument in arguments:
            if not isinstance(argument, ITypedArgument):
                return False
            argType = argTypes[idx]
            idx += 1
            if argType != argument.getType():
                return False
        return True
