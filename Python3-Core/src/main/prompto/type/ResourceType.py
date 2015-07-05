from prompto.type.CategoryType import CategoryType


class ResourceType ( CategoryType ):

	def __init__(self, name):
		super(ResourceType, self).__init__(name)

	def __eq__(self, obj):
		if id(obj)==id(self):
			return True
		if obj is None:
			return False
		if not isinstance(obj, ResourceType):
			return False
		return self.getName()==obj.getName()

	def isAssignableTo(self, context, other):
		return self==other
