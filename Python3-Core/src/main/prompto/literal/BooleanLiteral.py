from prompto.literal.Literal import Literal
from prompto.type.BooleanType import BooleanType
from prompto.value.Boolean import Boolean


class BooleanLiteral ( Literal ):

	def __init__(self, text):
		super(BooleanLiteral, self).__init__(text, Boolean.Parse(text))
	
	def check(self, context):
		return BooleanType.instance
