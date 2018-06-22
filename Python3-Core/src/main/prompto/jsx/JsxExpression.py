from prompto.jsx.IJsxExpression import IJsxExpression


class JsxExpression(IJsxExpression):

	def __init__(self, expression):
		super().__init__()
		self.expression = expression


	def check(self, context):
		return self.expression.check(context)


	def toDialect(self, writer):
		writer.append("{")
		self.expression.toDialect(writer)
		writer.append("}")
