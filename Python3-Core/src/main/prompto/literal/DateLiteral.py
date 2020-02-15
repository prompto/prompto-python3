from datetime import date

from prompto.literal.Literal import Literal
from prompto.type.DateType import DateType
from prompto.value.DateValue import DateValue


class DateLiteral ( Literal ):

	def __init__(self, text):
		super(DateLiteral, self).__init__(text, DateValue.Parse(text[1:-1]))
	
	def check(self, context):
		return DateType.instance
