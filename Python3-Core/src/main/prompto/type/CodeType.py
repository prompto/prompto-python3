from prompto.type.NativeType import NativeType


class CodeType ( NativeType ):

	instance = None
	
	def __init__(self):
		super(CodeType, self).__init__("Code")

CodeType.instance = CodeType()
