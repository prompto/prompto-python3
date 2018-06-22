from prompto.expression.IExpression import IExpression

from prompto.value.JsxValue import JsxValue


class IJsxExpression(IExpression):

	def interpret(self, context):
		return JsxValue(self)
