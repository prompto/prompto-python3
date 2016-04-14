from prompto.error.ExecutionError import ExecutionError


class NotMutableError(ExecutionError):

    def getExpression(self, context):
        from prompto.expression.CategorySymbol import CategorySymbol
        return context.getRegisteredValue(CategorySymbol, "NOT_MUTABLE")
