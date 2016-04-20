from prompto.error.ExecutionError import ExecutionError
from prompto.expression.CategorySymbol import CategorySymbol


class ReadWriteError ( ExecutionError ) :

    def __init__(self, message):
        super().__init__(message)

    def getExpression(self, context):
        return context.getRegisteredValue(CategorySymbol, "READ_WRITE")
