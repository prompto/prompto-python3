from presto.type.BooleanType import BooleanType
from presto.type.NativeType import NativeType


class CollectionType ( NativeType ) :

    def __init__(self, name, itemType):
        super(CollectionType, self).__init__(name)
        self.itemType = itemType

    def getItemType(self):
        return self.itemType

    def checkExists(self, context):
        self.itemType.checkExists(context)

    def checkContains(self, context, other):
        if self.itemType.isAssignableTo(context, other):
            return BooleanType.instance
        else:
            return super(CollectionType, self).checkContains(context, other)
