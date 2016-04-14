from prompto.error.ExecutionError import ExecutionError


class NullReferenceError(ExecutionError):

    def getExpression(self, context):
        from prompto.expression.CategorySymbol import CategorySymbol
        return context.getRegisteredValue(CategorySymbol, "NULL_REFERENCE")
