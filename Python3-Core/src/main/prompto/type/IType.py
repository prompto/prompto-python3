class IType(object):

	def anyfy(self):
		return self

	def resolve(self, context, onError = None):
		return self
