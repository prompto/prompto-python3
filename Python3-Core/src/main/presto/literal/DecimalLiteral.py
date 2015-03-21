from presto.literal.Literal import Literal
from presto.type.DecimalType import DecimalType
from presto.value.Decimal import Decimal


class DecimalLiteral ( Literal ):

	def __init__(self, text):
		super(DecimalLiteral, self).__init__(text,Decimal.Parse(text))

	def check(self, context):
		return DecimalType.instance
	

