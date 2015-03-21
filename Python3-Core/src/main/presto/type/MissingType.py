from presto.type.NativeType import NativeType


class MissingType ( NativeType ):

	instance = None
	
	def __init__(self):
		super(MissingType, self).__init__("*")

	def isAssignableTo(self, context, other):
		return True

MissingType.instance = MissingType()
	
