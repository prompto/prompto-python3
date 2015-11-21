from prompto.type.IterableType import IterableType
from prompto.type.IntegerType import IntegerType

class CursorType(IterableType):

    def __init__(self, itemType):
        super().__init__("Cursor<" + itemType.getName()+">", itemType)

    def isAssignableTo(self, context, other):
        return isinstance(other, CursorType) and self.itemType.isAssignableTo(context, other.itemType)

    def __eq__(self, obj):
        if obj is self:
            return True
        if not isinstance(obj, CursorType):
            return False
        return self.itemType==obj.itemType

    def checkIterator(self, context):
        return self.itemType

    def checkMember(self, context, name):
        if "length"==name:
            return IntegerType.instance
        else:
            return super().checkMember(context, name)
