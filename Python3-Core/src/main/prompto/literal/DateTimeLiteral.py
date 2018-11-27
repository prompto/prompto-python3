from prompto.literal.Literal import Literal
from prompto.type.DateTimeType import DateTimeType
from prompto.value.DateTime import DateTime


class DateTimeLiteral ( Literal ):
	
	def __init__(self, text):
		dt = DateTime.Parse(text[1:-1])
		super(DateTimeLiteral, self).__init__(text, dt)
	
	def check(self, context):
		return DateTimeType.instance
	
