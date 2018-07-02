class CssCode(object):

	def __init__(self, expression):
		self.expression = expression

	def toDialect(self, writer):
		writer.append("{")
		self.expression.toDialect(writer)
		writer.append("}")
