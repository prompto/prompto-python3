from prompto.type.NativeType import NativeType

class VoidType (NativeType):

    instance = None

    def __init__(self):
        super(VoidType, self).__init__("Void")


    def isAssignableTo(self, context, other):
        raise Exception("Should never get there !")

VoidType.instance = VoidType()	