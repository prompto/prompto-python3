from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily



class VoidType (NativeType):

    instance = None

    def __init__(self):
        super().__init__(TypeFamily.VOID)


    def isAssignableTo(self, context, other):
        raise Exception("Should never get there !")

VoidType.instance = VoidType()	