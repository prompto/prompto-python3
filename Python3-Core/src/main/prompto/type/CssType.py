from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily


class CssType(NativeType):

	instance = None

	def __init__(self):
		super().__init__(TypeFamily.CSS)


	def checkAdd(self, context, other, tryReverse):
		if other is self:
			return self
		else:
			super().checkAdd(context, other, tryReverse)

CssType.instance = CssType()