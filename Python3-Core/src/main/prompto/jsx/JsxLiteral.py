from prompto.type.TextType import TextType


class JsxLiteral(object):

	def __init__(self, text):
		self.text = text

	
	def check(self, context):
		return TextType.instance

	
	def toDialect(self, writer):
		writer.append(self.text)

