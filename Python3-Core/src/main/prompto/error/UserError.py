from prompto.error.ExecutionError import ExecutionError


class UserError ( ExecutionError ):

	def __init__(self, expression):
		self.expression = expression
	
	def getExpression(self, context):
		return self.expression
