from prompto.type.NativeType import NativeType


class IterableType ( NativeType ) :

    def __init__(self, name, itemType):
        super().__init__(name)
        self.itemType = itemType

    def getItemType(self):
        return self.itemType

    def checkExists(self, context):
        self.itemType.checkExists(context)

