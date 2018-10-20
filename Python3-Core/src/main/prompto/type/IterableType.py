from prompto.type.IType import IType
from prompto.type.NativeType import NativeType


class IterableType ( NativeType ) :

    def __init__(self, family, itemType):
        super().__init__(family)
        self.itemType = itemType


    def withItemType(self, itemType: IType):
        raise Exception("missing withItemType " + type(self).__name__)


    def checkExists(self, context):
        self.itemType.checkExists(context)


    def isMoreSpecificThan(self, context, other):
        return isinstance(other, IterableType) and \
            self.itemType.isMoreSpecificThan(context, other.itemType)
