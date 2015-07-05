from prompto.type.NativeType import NativeType

class AnyType ( NativeType ): 

	instance = None
	
	def __init__(self):
		super(AnyType, self).__init__("any")
	
	def checkItem(self, context, itemType):
		return AnyType.instance # needed to support lists in Documents

	def checkMember(self, context, name):
		return AnyType.instance # needed to support members in Documents

	def isAssignableTo(self, context, other):
		return isinstance(other, AnyType)

AnyType.instance = AnyType()