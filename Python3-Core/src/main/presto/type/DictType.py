from presto.type.BooleanType import BooleanType
from presto.type.CollectionType import CollectionType
from presto.type.EntryType import EntryType
from presto.type.IntegerType import IntegerType
from presto.type.ListType import ListType
from presto.type.TextType import TextType


class DictType ( CollectionType ):

    def __init__(self, itemType):
        super(DictType, self).__init__(itemType.getName()+"{}",itemType)

    def isAssignableTo(self, context, other):
        return isinstance(other, DictType) and self.itemType.isAssignableTo(context, other.getItemType())

    def __eq__(self, obj):
        if id(obj)==id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, DictType):
            return False
        return self.getItemType()==obj.getItemType()

    def checkAdd(self, context, other, tryReverse):
        if isinstance(other, DictType) and self.getItemType()==other.getItemType():
            return self
        else:
            return super(DictType, self).checkAdd(context, other, tryReverse)

    def checkContains(self, context, other):
        if other==TextType.instance:
            return BooleanType.instance
        else:
            return super(DictType, self).checkContains(context, other)

    def checkItem(self, context, other):
        if other==TextType.instance:
            return self.itemType
        else:
            return super(DictType, self).checkItem(context,other)

    def checkIterator(self, context):
        return EntryType(self.itemType)

    def checkMember(self, context, name):
        if "length"==name:
            return IntegerType.instance
        elif "keys"==name:
            return ListType(TextType.instance)
        elif "values"==name:
            return ListType(self.itemType)
        else:
            return super(DictType, self).checkMember(context, name)
