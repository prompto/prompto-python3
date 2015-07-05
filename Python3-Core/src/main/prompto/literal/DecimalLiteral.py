from prompto.literal.Literal import Literal
from prompto.type.DecimalType import DecimalType
from prompto.value.Decimal import Decimal


class DecimalLiteral ( Literal ):

	def __init__(self, text):
		super(DecimalLiteral, self).__init__(text,Decimal.Parse(text))

	def check(self, context):
		return DecimalType.instance
	

