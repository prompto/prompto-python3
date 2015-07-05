from prompto.error.PrestoError import PrestoError


class ExecutionError(PrestoError):

    def __init__(self, message=None, exception=None):
        super().__init__(message, exception)

    def interpret(self, context, errorName):
        from prompto.expression.ConstructorExpression import ConstructorExpression
        from prompto.grammar.ArgumentAssignment import ArgumentAssignment
        from prompto.grammar.ArgumentAssignmentList import ArgumentAssignmentList
        from prompto.grammar.UnresolvedArgument import UnresolvedArgument
        from prompto.literal.TextLiteral import TextLiteral
        from prompto.type.CategoryType import CategoryType
        exp = self.getExpression(context)
        if exp is None:
            args = ArgumentAssignmentList()
            args.add(ArgumentAssignment(UnresolvedArgument("name"), TextLiteral(type(self).__name__)))
            args.add(ArgumentAssignment(UnresolvedArgument("text"), TextLiteral(self.message)))
            exp = ConstructorExpression(CategoryType("Error"), args)
        if context.getRegisteredValue(object, errorName) is None:
            from prompto.runtime.ErrorVariable import ErrorVariable
            context.registerValue(ErrorVariable(errorName))
        error = exp.interpret(context)
        context.setValue(errorName, error)
        return error
