from datetime import date

from presto.literal.Literal import Literal
from presto.type.DateType import DateType
from presto.value.Date import Date


class DateLiteral ( Literal ):

	def __init__(self, text):
		super(DateLiteral, self).__init__(text, Date.Parse(text[1:-1]))
	
	def check(self, context):
		return DateType.instance
