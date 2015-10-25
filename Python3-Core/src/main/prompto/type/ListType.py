from prompto.type.AnyType import AnyType
from prompto.type.BooleanType import BooleanType
from prompto.type.ContainerType import ContainerType


class ListType(ContainerType):

    def __init__(self, itemType):
        super(ListType, self).__init__(itemType.getName() + "[]", itemType)

    def isAssignableTo(self, context, other):
        return isinstance(other, AnyType) or \
               (isinstance(other, ListType) and self.itemType.isAssignableTo(context, other.getItemType()))

    def __eq__(self, obj):
        if id(obj) == id(self):
            return True
        if obj == None:
            return False
        if not isinstance(obj, ListType):
            return False
        return self.getItemType() == obj.getItemType()

    def checkAdd(self, context, other, tryReverse):
        if isinstance(other, ListType) and self.getItemType() == other.getItemType():
            return self
        else:
            return super(ListType, self).checkAdd(context, other, tryReverse)

    def checkItem(self, context, other):
        from prompto.type.IntegerType import IntegerType
        if other == IntegerType.instance:
            return self.itemType
        else:
            return super(ListType, self).checkItem(context, other)

    def checkSlice(self, context):
        return self

    def checkMultiply(self, context, other, tryReverse):
        from prompto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return self
        return super(ListType, self).checkMultiply(context, other, tryReverse)

    def checkContainsAllOrAny(self, context, other):
        return BooleanType.instance

    def checkIterator(self, context):
        return self.itemType

    def checkMember(self, context, name):
        from prompto.type.IntegerType import IntegerType
        if "length" == name:
            return IntegerType.instance
        else:
            return super(ListType, self).checkMember(context, name)

