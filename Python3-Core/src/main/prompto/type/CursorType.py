from prompto.type.ContainerType import ContainerType
from prompto.type.IntegerType import IntegerType

class CursorType(ContainerType):

    def __init__(self, itemType):
        super().__init__(itemType.getName()+"[]", itemType)

    def isAssignableTo(self, context, other):
        return isinstance(other, CursorType) and self.itemType.isAssignableTo(context, other.itemType)

    def __eq__(self, obj):
        if obj is self:
            return True
        if not isinstance(obj, CursorType):
            return False
        return this.itemType==other.itemType

    def checkIterator(self, context):
        return self.itemType

    def checkMember(self, context, name):
        if "length"==name:
            return IntegerType.instance
        else:
            return super().checkMember(context, name)
