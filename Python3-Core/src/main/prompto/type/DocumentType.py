from prompto.type.AnyType import AnyType
from prompto.type.NativeType import NativeType


class DocumentType ( NativeType ):
	
	instance = None
	
	def __init__(self):
		super(DocumentType, self).__init__("Document")

	def isAssignableTo(self, context, other):
		return isinstance(other, DocumentType) or isinstance(other, AnyType)

	def checkMember(self, context, name):
		return AnyType.instance

DocumentType.instance = DocumentType()

