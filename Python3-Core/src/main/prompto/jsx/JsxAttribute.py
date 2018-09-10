class JsxAttribute(object):

	def __init__(self, name, value, suite):
		super(JsxAttribute, self).__init__()
		self.name = name
		self.value = value
		self.suite = suite

	def check(self, context):
		if self.value is not None:
			self.value.check(context)

	def toDialect(self, writer):
		writer.append(self.name)
		if self.value is not None:
			writer.append("=")
			self.value.toDialect(writer)
		if self.suite is not None:
			writer.appendRaw(self.suite)
		else:
			writer.append(" ")