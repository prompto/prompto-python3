from presto.error.PrestoError import PrestoError
from presto.expression.ConstructorExpression import ConstructorExpression
from presto.grammar.ArgumentAssignment import ArgumentAssignment
from presto.grammar.ArgumentAssignmentList import ArgumentAssignmentList
from presto.grammar.UnresolvedArgument import UnresolvedArgument
from presto.literal.TextLiteral import TextLiteral
from presto.type.CategoryType import CategoryType


class ExecutionError(PrestoError):

    def __init__(self, message=None, exception=None):
        super().__init__(message, exception)

    def interpret(self, context, errorName):
        exp = self.getExpression(context)
        if exp is None:
            args = ArgumentAssignmentList()
            args.add(ArgumentAssignment(UnresolvedArgument("name"), TextLiteral(type(self).__name__)))
            args.add(ArgumentAssignment(UnresolvedArgument("text"), TextLiteral(self.message)))
            exp = ConstructorExpression(CategoryType("Error"), args)
        if context.getRegisteredValue(object, errorName) is None:
            from presto.runtime.ErrorVariable import ErrorVariable
            context.registerValue(ErrorVariable(errorName))
        error = exp.interpret(context)
        context.setValue(errorName, error)
        return error
