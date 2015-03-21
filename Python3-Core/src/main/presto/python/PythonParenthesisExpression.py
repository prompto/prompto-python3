from presto.python.PythonExpression import PythonExpression

class PythonParenthesisExpression ( PythonExpression ):

	def __init__(self, expression):
		super(PythonParenthesisExpression, self).__init__()
		self.expression = expression;
