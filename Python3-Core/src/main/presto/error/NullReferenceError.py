from presto.error.ExecutionError import ExecutionError


class NullReferenceError(ExecutionError):

    def getExpression(self, context):
        from presto.grammar.CategorySymbol import CategorySymbol
        return context.getRegisteredValue(CategorySymbol, "NULL_REFERENCE")
