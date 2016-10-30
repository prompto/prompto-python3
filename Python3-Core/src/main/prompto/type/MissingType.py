from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily



class MissingType ( NativeType ):

    instance = None

    def __init__(self):
        super(MissingType, self).__init__(TypeFamily.MISSING)
        self.typeName = "*"


    def isAssignableTo(self, context, other):
        return True

MissingType.instance = MissingType()

