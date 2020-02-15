from datetime import date

from prompto.literal.Literal import Literal
from prompto.type.DateType import DateType
from prompto.type.VersionType import VersionType
from prompto.value.DateValue import DateValue
from prompto.value.VersionValue import VersionValue


class VersionLiteral ( Literal ):

	def __init__(self, text):
		super(VersionLiteral, self).__init__(text, VersionValue.Parse(text[2:-1]))
	
	def check(self, context):
		return VersionType.instance
