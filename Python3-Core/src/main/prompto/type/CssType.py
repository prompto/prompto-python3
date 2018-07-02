from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily


class CssType(NativeType):

	def __init__(self):
		super().__init__(TypeFamily.CSS)

CssType.instance = CssType()