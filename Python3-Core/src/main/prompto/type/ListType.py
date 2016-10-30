from prompto.type.AnyType import AnyType
from prompto.type.BooleanType import BooleanType
from prompto.type.ContainerType import ContainerType
from prompto.store.TypeFamily import TypeFamily



class ListType(ContainerType):

    def __init__(self, itemType):
        super().__init__(TypeFamily.LIST, itemType)
        self.typeName = itemType.typeName + "[]"

    def isAssignableTo(self, context, other):
        return isinstance(other, AnyType) or \
               (isinstance(other, ListType) and self.itemType.isAssignableTo(context, other.getItemType()))

    def __eq__(self, obj):
        if id(obj) == id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, ListType):
            return False
        return self.getItemType() == obj.getItemType()

    def checkAdd(self, context, other, tryReverse):
        from prompto.type.SetType import SetType
        if isinstance(other, (ListType, SetType)) and self.getItemType() == other.getItemType():
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
        if "count" == name:
            return IntegerType.instance
        else:
            return super(ListType, self).checkMember(context, name)

    def convertPythonValueToPromptoValue(self, context, value, returnType):
        if isinstance(value, (list, set, tuple)):
            items = [self.itemType.convertPythonValueToPromptoValue(context, item, returnType) for item in value]
            from prompto.value.ListValue import ListValue
            return ListValue(self.itemType, items=items)
        else:
            return super(ListType, self).convertPythonValueToPromptoValue(context, value, returnType)
