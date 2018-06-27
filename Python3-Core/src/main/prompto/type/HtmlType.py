from prompto.type.IType import IType
from prompto.type.JsxType import JsxType
from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily


class HtmlType(NativeType):

    def __init__(self):
        super().__init__(TypeFamily.HTML)


    def isAssignableFrom(self, context, other:IType):
        if other == JsxType.instance:
            return True
        else:
            return super().isAssignableFrom(context, other)

HtmlType.instance = HtmlType()