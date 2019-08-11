from io import StringIO
import os

from prompto.declaration.BaseDeclaration import *
from prompto.declaration.IMethodDeclaration import IMethodDeclaration
from prompto.error.SyntaxError import SyntaxError
from prompto.grammar.Argument import Argument


class BaseMethodDeclaration(BaseDeclaration, IMethodDeclaration):

    def __init__(self, name, arguments, returnType=None):
        super().__init__(name)
        from prompto.param.ParameterList import ParameterList
        self.arguments = arguments if arguments is not None else ParameterList()
        self.returnType = returnType
        self.memberOf = None
        self.closureOf = None

    def getSignature(self, dialect):
        with StringIO() as sb:
            try:
                sb.write(self.getName())
                sb.write('(')
                for arg in self.arguments:
                    sb.write(arg.getSignature(dialect))
                    sb.write(", ")
                if self.arguments.size() > 0:
                    sb.seek(-2, os.SEEK_CUR)  # strip ", "
                sb.write(')')
                return sb.getvalue()
            finally:
                sb.close()


    def __str__(self):
        return self.getName() + ":(" + str(self.arguments) + ')'

    def getProto(self):
        with StringIO() as sb:
            for arg in self.arguments:
                sb.write(arg.getProto())
                sb.write('/')
            val = sb.getvalue()
        if len(val) > 0:
            val = val[:-1]  # strip "/"
        return val

    def getArguments(self):
        return self.arguments

    def getReturnType(self):
        return self.returnType

    def register(self, context):
        context.registerMethodDeclaration(self)

    def registerArguments(self, context):
        self.arguments.register(context)

    def getType(self, context):
        try:
            return self.check(context)
        except SyntaxError as e:
            raise Exception(e)

    def isAssignableTo(self, context, arguments, checkInstance):
        from prompto.grammar.ArgumentList import ArgumentList
        try:
            local = context.newLocalContext()
            self.registerArguments(local)
            argumentsList = ArgumentList(items=arguments)
            for argument in self.arguments:
                found = argumentsList.find(argument.getName())
                toRemove = found
                if found is None:  # missing argument
                    if argument.defaultExpression is None:
                        return False
                    found = Argument(argument, argument.defaultExpression)
                if not self.isArgAssignableTo(local, argument, found, checkInstance):
                    return False
                if toRemove is not None:
                    argumentsList.remove(toRemove)
            return len(argumentsList)==0
        except SyntaxError:
            return False


    def isArgAssignableTo(self, context, parameter, argument, checkInstance):
        from prompto.grammar.Specificity import Specificity
        return self.computeSpecificity(context, parameter, argument, checkInstance) != Specificity.INCOMPATIBLE


    def computeSpecificity(self, context, parameter, argument, checkInstance):
        from prompto.error.PromptoError import PromptoError
        from prompto.grammar.Specificity import Specificity
        from prompto.type.CategoryType import CategoryType
        from prompto.value.IInstance import IInstance

        try:
            required = parameter.getType(context)
            actual = argument.getExpression().check(context)
            # retrieve actual runtime type
            if checkInstance and isinstance(actual, CategoryType):
                value = argument.getExpression().interpret(context.getCallingContext())
                if isinstance(value, IInstance):
                    actual = value.getType()
            if actual == required:
                return Specificity.EXACT
            if required.isAssignableFrom(context, actual):
                return Specificity.INHERITED
            actual = argument.resolve(context, self, checkInstance).check(context)
            if required.isAssignableFrom(context, actual):
                return Specificity.RESOLVED
        except PromptoError:
            pass
        return Specificity.INCOMPATIBLE


    def interpret(self, context):
        from prompto.error.InternalError import InternalError

        raise InternalError("Should never get there!")


    def isEligibleAsMain(self):
        return False

