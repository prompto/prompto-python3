from prompto.jsx.IJsxExpression import IJsxExpression
from prompto.type.JsxType import JsxType


class JsxCode(IJsxExpression):

	def __init__(self, expression, suite):
		super().__init__()
		self.expression = expression
		self.suite = suite


	def check(self, context):
		self.expression.check(context)
		return JsxType.instance


	def toDialect(self, writer):
		writer.append("{")
		self.expression.toDialect(writer)
		writer.append("}")
		if self.suite is not None:
			writer.appendRaw(self.suite)
