class CssText(object):

	def __init__(self, text):
		self.text = text

	def toDialect(self, writer):
		writer.append(self.text)

