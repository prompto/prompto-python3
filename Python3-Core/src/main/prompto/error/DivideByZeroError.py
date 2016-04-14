from prompto.error.ExecutionError import ExecutionError
from prompto.expression.CategorySymbol import CategorySymbol


class DivideByZeroError ( ExecutionError ) :

	def getExpression(self, context):
		return context.getRegisteredValue(CategorySymbol, "DIVIDE_BY_ZERO")
