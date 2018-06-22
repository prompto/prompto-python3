from prompto.jsx.IJsxExpression import IJsxExpression


class JsxCode(IJsxExpression):

	def __init__(self, expression):
		super().__init__()
		self.expression = expression

	
	def check(self, context):
		self.expression.check(context)
		return JsxType.instance


	def toDialect(self, writer):
		writer.append("{")
		self.expression.toDialect(writer)
		writer.append("}")
