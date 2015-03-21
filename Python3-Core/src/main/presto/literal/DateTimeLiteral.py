from presto.literal.Literal import *
from presto.type.DateTimeType import *
from presto.value.DateTime import *


class DateTimeLiteral ( Literal ):
	
	def __init__(self, text):
		dt = DateTimeLiteral.parseDateTime(text[1:-1])
		super(DateTimeLiteral, self).__init__(text, dt)
	
	def check(self, context):
		return DateTimeType.instance
	
	@staticmethod
	def parseDateTime(text):
		year = int(text[0:4])
		text = text[5:]
		month = int(text[0:2])
		text = text[3:]
		day = int(text[0:2])
		text = text[3:]
		if len(text)>0:
			hour = int(text[0:2])
			text = text[3:]
		else:
			hour = 0
		if len(text)>0:
			minute = int(text[0:2])
			text = text[3:]
		else:
			minute = 0
		if len(text)>0:
			second = int(text[0:2])
			text = text[2:]
		else:
			second = 0
		if len(text)>0 and text[0]=='.':
			text = text[1:]
			buffer = ""
			while len(text)>0 and text[0]>='0' and text[0]<='9':
				buffer += text[0]
				text = text[1:]
			while len(buffer)<6:
				buffer += '0'
			micro = int(buffer)
		else:
			micro = 0
		zone = None
		dt = datetime(year,month,day,hour,minute,second,micro,zone)
		return DateTime(value=dt)
