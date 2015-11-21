from prompto.type.IterableType import IterableType
from prompto.type.IntegerType import IntegerType

class IteratorType(IterableType):

    def __init__(self, itemType):
        super().__init__("Iterator<" + itemType.getName()+">", itemType)

    def isAssignableTo(self, context, other):
        return isinstance(other, IteratorType) and self.itemType.isAssignableTo(context, other.itemType)

    def __eq__(self, obj):
        if obj is self:
            return True
        if not isinstance(obj, IteratorType):
            return False
        return self.itemType==obj.itemType

    def checkIterator(self, context):
        return self.itemType
