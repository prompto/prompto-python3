from io import StringIO
import os

from prompto.declaration.BaseDeclaration import *
from prompto.declaration.IMethodDeclaration import IMethodDeclaration
from prompto.error.SyntaxError import SyntaxError
from prompto.grammar.ArgumentAssignment import ArgumentAssignment


class BaseMethodDeclaration(BaseDeclaration, IMethodDeclaration):

    def __init__(self, name, arguments, returnType=None):
        super().__init__(name)
        from prompto.grammar.ArgumentList import ArgumentList
        self.arguments = arguments if arguments is not None else ArgumentList()
        self.returnType = returnType
        self.memberOf = None

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

    def isAssignableTo(self, context, assignments, checkInstance):
        from prompto.grammar.ArgumentAssignmentList import ArgumentAssignmentList
        try:
            local = context.newLocalContext()
            self.registerArguments(local)
            assignmentsList = ArgumentAssignmentList(list_=assignments)
            for argument in self.arguments:
                assignment = assignmentsList.find(argument.getName())
                toRemove = assignment
                if assignment is None:  # missing argument
                    if argument.defaultExpression is None:
                        return False
                    assignment = ArgumentAssignment(argument, argument.defaultExpression)
                if not self.isArgAssignableTo(local, argument, assignment, checkInstance):
                    return False
                if toRemove is not None:
                    assignmentsList.remove(toRemove)
            return len(assignmentsList)==0
        except SyntaxError:
            return False

    def isArgAssignableTo(self, context, argument, assignment, checkInstance):
        from prompto.grammar.Specificity import Specificity
        return self.computeSpecificity(context, argument, assignment, checkInstance) != Specificity.INCOMPATIBLE

    def computeSpecificity(self, context, argument, assignment, checkInstance):
        from prompto.error.PromptoError import PromptoError
        from prompto.grammar.Specificity import Specificity
        from prompto.type.CategoryType import CategoryType
        from prompto.value.IInstance import IInstance

        try:
            required = argument.getType(context)
            actual = assignment.getExpression().check(context)
            # retrieve actual runtime type
            if checkInstance and isinstance(actual, CategoryType):
                value = assignment.getExpression().interpret(context.getCallingContext())
                if isinstance(value, IInstance):
                    actual = value.getType()
            if actual == required:
                return Specificity.EXACT
            if required.isAssignableFrom(context, actual):
                return Specificity.INHERITED
            actual = assignment.resolve(context, self, checkInstance).check(context)
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

