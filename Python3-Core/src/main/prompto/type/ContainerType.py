from prompto.type.BooleanType import BooleanType
from prompto.type.NativeType import NativeType


class ContainerType ( NativeType ) :

    def __init__(self, name, itemType):
        super(ContainerType, self).__init__(name)
        self.itemType = itemType

    def getItemType(self):
        return self.itemType

    def checkExists(self, context):
        self.itemType.checkExists(context)

    def checkContains(self, context, other):
        if self.itemType.isAssignableTo(context, other):
            return BooleanType.instance
        else:
            return super(ContainerType, self).checkContains(context, other)
