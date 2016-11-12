from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily


class AnyType ( NativeType ): 

    instance = None

    def __init__(self):
        super(AnyType, self).__init__(TypeFamily.ANY)
        self.typeName = "any"

    def checkItem(self, context, itemType):
        return AnyType.instance # needed to support lists in Documents

    def checkMember(self, context, name):
        return AnyType.instance # needed to support members in Documents

    def isAssignableFrom(self, context, other):
        return True

AnyType.instance = AnyType()