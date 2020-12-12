class CssText(object):

	def __init__(self, text):
		self.text = text


	def toDialect(self, writer):
		writer.append(self.text)


	def __str__(self):
		return self.text