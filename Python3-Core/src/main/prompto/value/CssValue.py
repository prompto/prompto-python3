from prompto.value.BaseValue import BaseValue
from prompto.type.CssType import CssType


class CssValue(BaseValue):

	def __init__(self, expression):
		super().__init__(CssType.instance)
		self.expression = expression
