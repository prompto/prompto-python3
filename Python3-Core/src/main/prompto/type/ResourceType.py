from prompto.type.CategoryType import CategoryType
from prompto.store.TypeFamily import TypeFamily



class ResourceType ( CategoryType ):

	def __init__(self, name):
		super().__init__(name, TypeFamily.RESOURCE)

	def __eq__(self, obj):
		if id(obj)==id(self):
			return True
		if obj is None:
			return False
		if not isinstance(obj, ResourceType):
			return False
		return self.typeName == obj.typeName

	def isAssignableTo(self, context, other):
		return self==other
