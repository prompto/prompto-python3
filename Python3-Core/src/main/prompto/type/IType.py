class IType(object):

	def anyfy(self):
		return self

	def resolve(self, context, onError = None):
		return self

	def isMutable(self, context):
		return False

	def asMutable(self, context, mutable:bool):
		if mutable:
			raise SyntaxError("Cannot mutate " + self.typeName)
		else:
			return self