from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily



class CodeType ( NativeType ):

	instance = None
	
	def __init__(self):
		super(CodeType, self).__init__(TypeFamily.CODE)

CodeType.instance = CodeType()
