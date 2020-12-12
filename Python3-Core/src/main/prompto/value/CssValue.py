from prompto.value.BaseValue import BaseValue
from prompto.type.CssType import CssType


class CssValue(BaseValue):

	def __init__(self, expression):
		super().__init__(CssType.instance)
		self.expression = expression

	def Add(self, context, value):
		if isinstance(value, CssValue):
			return self.expression.plus(value.expression)
		else:
			raise SyntaxError("Illegal: Css + " + type(value).__name__)
