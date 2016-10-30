from prompto.type.IterableType import IterableType
from prompto.store.TypeFamily import TypeFamily



class IteratorType(IterableType):

    def __init__(self, itemType):
        super().__init__(TypeFamily.ITERATOR, itemType)
        self.typeName = "Iterator<" + itemType.typeName + ">"

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
