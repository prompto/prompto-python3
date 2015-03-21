from presto.error.ExecutionError import ExecutionError
from presto.grammar.CategorySymbol import CategorySymbol


class IndexOutOfRangeError ( ExecutionError ):

	def getExpression(self, context):
		return context.getRegisteredValue(CategorySymbol, "INDEX_OUT_OF_RANGE")
