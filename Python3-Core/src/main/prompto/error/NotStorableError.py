from prompto.error.ExecutionError import ExecutionError


class NotStorableError(ExecutionError):

    def getExpression(self, context):
        from prompto.grammar.CategorySymbol import CategorySymbol
        return context.getRegisteredValue(CategorySymbol, "NOT_STORABLE")
