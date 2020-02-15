from prompto.literal.Literal import Literal
from prompto.type.BooleanType import BooleanType
from prompto.value.BooleanValue import BooleanValue


class BooleanLiteral ( Literal ):

	def __init__(self, text):
		super(BooleanLiteral, self).__init__(text, BooleanValue.Parse(text))
	
	def check(self, context):
		return BooleanType.instance
