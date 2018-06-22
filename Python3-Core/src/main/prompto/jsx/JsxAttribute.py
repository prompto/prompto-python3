class JsxAttribute(object):

	def __init__(self, name, value):
		super().__init__()
		self.name = name
		self.value = value


	def check(self, context):
		if self.value is not None:
			self.value.check(context)


	def toDialect(self, writer):
		writer.append(" ").append(self.name)
		if self.value is not None:
			writer.append("=")
			self.value.toDialect(writer)
