from prompto.java.JavaExpression import JavaExpression


class JavaParenthesisExpression ( JavaExpression ):

	def __init__(self, expression):
		super(JavaParenthesisExpression, self).__init__()
		self.expression = expression;
