from presto.error.ExecutionError import ExecutionError


class NotMutableError(ExecutionError):

    def getExpression(self, context):
        from presto.grammar.CategorySymbol import CategorySymbol
        return context.getRegisteredValue(CategorySymbol, "NOT_MUTABLE")
