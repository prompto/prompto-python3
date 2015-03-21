from presto.error.ExecutionError import ExecutionError
from presto.grammar.CategorySymbol import CategorySymbol


class DivideByZeroError ( ExecutionError ) :

	def getExpression(self, context):
		return context.getRegisteredValue(CategorySymbol, "DIVIDE_BY_ZERO")
