from prompto.error.PromptoError import PromptoError


class ExecutionError(PromptoError):

    def __init__(self, message=None, exception=None):
        super().__init__(message, exception)

    def interpret(self, context, errorName):
        from prompto.expression.ConstructorExpression import ConstructorExpression
        from prompto.grammar.Argument import Argument
        from prompto.grammar.ArgumentList import ArgumentList
        from prompto.param.UnresolvedParameter import UnresolvedParameter
        from prompto.literal.TextLiteral import TextLiteral
        from prompto.type.CategoryType import CategoryType
        exp = self.getExpression(context)
        if exp is None:
            args = ArgumentList()
            args.add(Argument(UnresolvedParameter("name"), TextLiteral(type(self).__name__)))
            args.add(Argument(UnresolvedParameter("text"), TextLiteral(self.message)))
            exp = ConstructorExpression(CategoryType("Error"), args)
        if context.getRegisteredValue(object, errorName) is None:
            from prompto.runtime.ErrorVariable import ErrorVariable
            context.registerValue(ErrorVariable(errorName))
        error = exp.interpret(context)
        context.setValue(errorName, error)
        return error
