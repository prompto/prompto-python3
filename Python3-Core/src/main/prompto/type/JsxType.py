from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily


class JsxType(NativeType):

	instance = None

	def __init__(self):
		super().__init__(TypeFamily.JSX)

JsxType.instance = JsxType()