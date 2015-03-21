from presto.type.BooleanType import BooleanType
from presto.type.CollectionType import CollectionType
from presto.value.IContainer import IContainer

class SetType(CollectionType):

    def __init__(self, itemType):
        super().__init__(itemType.getName() + "<>", itemType)

    def isAssignableTo(self, context, other):
        return isinstance(other, SetType) and self.itemType.isAssignableTo(context, other.getItemType())

    def __eq__(self, obj):
        if id(obj) == id(self):
            return True
        if obj == None:
            return False
        if not isinstance(obj, SetType):
            return False
        return self.getItemType() == obj.getItemType()

    def checkAdd(self, context, other, tryReverse):
        if isinstance(other, CollectionType) and self.getItemType() == other.getItemType():
            return self
        else:
            return super().checkAdd(context, other, tryReverse)

    def checkItem(self, context, other):
        from presto.type.IntegerType import IntegerType
        if other == IntegerType.instance:
            return self.itemType
        else:
            return super().checkItem(context, other)

    def checkContainsAllOrAny(self, context, other):
        return BooleanType.instance

    def checkIterator(self, context):
        return self.itemType

    def checkMember(self, context, name):
        from presto.type.IntegerType import IntegerType
        if "length" == name:
            return IntegerType.instance
        else:
            return super().checkMember(context, name)

