from prompto.type.IType import IType
from prompto.type.IterableType import IterableType
from prompto.store.TypeFamily import TypeFamily



class IteratorType(IterableType):

    def __init__(self, itemType):
        super().__init__(TypeFamily.ITERATOR, itemType)
        self.typeName = "Iterator<" + itemType.typeName + ">"


    def isAssignableFrom(self, context, other):
        return super().isAssignableFrom(context, other) or \
               (isinstance(other, IteratorType) and self.itemType.isAssignableFrom(context, other.itemType))


    def __eq__(self, obj):
        if obj is self:
            return True
        if not isinstance(obj, IteratorType):
            return False
        return self.itemType==obj.itemType


    def checkIterator(self, context):
        return self.itemType


    def withItemType(self, itemType:IType):
        return IteratorType(itemType)