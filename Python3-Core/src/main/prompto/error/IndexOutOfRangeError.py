from prompto.error.ExecutionError import ExecutionError
from prompto.expression.CategorySymbol import CategorySymbol


class IndexOutOfRangeError ( ExecutionError ):

	def getExpression(self, context):
		return context.getRegisteredValue(CategorySymbol, "INDEX_OUT_OF_RANGE")
