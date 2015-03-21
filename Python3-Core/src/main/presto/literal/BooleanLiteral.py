from presto.literal.Literal import Literal
from presto.type.BooleanType import BooleanType
from presto.value.Boolean import Boolean


class BooleanLiteral ( Literal ):

	def __init__(self, text):
		super(BooleanLiteral, self).__init__(text, Boolean.Parse(text))
	
	def check(self, context):
		return BooleanType.instance
