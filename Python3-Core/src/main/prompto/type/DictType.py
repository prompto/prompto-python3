from prompto.type.BooleanType import BooleanType
from prompto.type.ContainerType import ContainerType
from prompto.type.EntryType import EntryType
from prompto.type.IType import IType
from prompto.type.IntegerType import IntegerType
from prompto.type.ListType import ListType
from prompto.type.SetType import SetType
from prompto.type.TextType import TextType
from prompto.store.TypeFamily import TypeFamily



class DictType ( ContainerType ):

    def __init__(self, itemType):
        super(DictType, self).__init__(TypeFamily.DICTIONARY, itemType)
        self.typeName = itemType.typeName + "<:>"


    def isAssignableFrom(self, context, other):
        return super().isAssignableFrom(context, other) or \
               (isinstance(other, DictType) and self.itemType.isAssignableFrom(context, other.itemType))


    def __eq__(self, obj):
        if id(obj)==id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, DictType):
            return False
        return self.itemType==obj.itemType


    def checkAdd(self, context, other, tryReverse):
        if isinstance(other, DictType) and self.itemType==other.itemType:
            return self
        else:
            return super(DictType, self).checkAdd(context, other, tryReverse)


    def checkContains(self, context, other):
        if other==TextType.instance:
            return BooleanType.instance
        else:
            return super(DictType, self).checkContains(context, other)


    def checkContainsAllOrAny(self, context, other):
        return BooleanType.instance


    def checkItem(self, context, other):
        if other==TextType.instance:
            return self.itemType
        else:
            return super(DictType, self).checkItem(context,other)


    def checkIterator(self, context):
        return EntryType(self.itemType)


    def checkMember(self, context, name):
        if "count"==name:
            return IntegerType.instance
        elif "keys"==name:
            return SetType(TextType.instance)
        elif "values"==name:
            return ListType(self.itemType)
        else:
            return super(DictType, self).checkMember(context, name)

    def withItemType(self, itemType:IType):
        return DictType(itemType)