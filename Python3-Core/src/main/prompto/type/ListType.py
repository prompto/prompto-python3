from prompto.declaration.BuiltInMethodDeclaration import BuiltInMethodDeclaration
from prompto.error.NotMutableError import NotMutableError
from prompto.type.AnyType import AnyType
from prompto.type.BooleanType import BooleanType
from prompto.type.ContainerType import ContainerType, BaseJoinMethodDeclaration
from prompto.store.TypeFamily import TypeFamily
from prompto.type.IType import IType
from prompto.type.VoidType import VoidType


class ListType(ContainerType):

    def __init__(self, itemType):
        super().__init__(TypeFamily.LIST, itemType)
        self.typeName = itemType.typeName + "[]"


    def isAssignableFrom(self, context, other):
        return super().isAssignableFrom(context, other) or \
               (isinstance(other, ListType) and self.itemType.isAssignableFrom(context, other.itemType))


    def __eq__(self, obj):
        if id(obj) == id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, ListType):
            return False
        return self.itemType == obj.itemType


    def checkAdd(self, context, other, tryReverse):
        from prompto.type.SetType import SetType
        if isinstance(other, (ListType, SetType)) and self.itemType.isAssignableFrom(context, other.itemType):
            return self
        else:
            return super(ListType, self).checkAdd(context, other, tryReverse)


    def checkSubstract(self, context, other):
        from prompto.type.SetType import SetType
        if isinstance(other, (ListType, SetType)) and self.itemType == other.itemType:
            return self
        else:
            return super(ListType, self).checkSubstract(context, other)


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


    def getMemberMethods(self, context, name):
        if name == "join":
            return [JoinListMethodDeclaration()]
        elif name == "removeItem":
            return [RemoveItemMethodDeclaration()]
        elif name == "removeValue":
            return [RemoveValueMethodDeclaration()]
        else:
            return super().getMemberMethods(context, name)


    def convertPythonValueToPromptoValue(self, context, value, returnType):
        if isinstance(value, (list, set, tuple)):
            items = [self.itemType.convertPythonValueToPromptoValue(context, item, returnType) for item in value]
            from prompto.value.ListValue import ListValue
            return ListValue(self.itemType, items=items)
        else:
            return super(ListType, self).convertPythonValueToPromptoValue(context, value, returnType)


    def withItemType(self, itemType:IType):
        return ListType(itemType)



class JoinListMethodDeclaration(BaseJoinMethodDeclaration):

    def getItems(self, context):
        return self.getValue(context).items


class RemoveItemMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        from prompto.type.IntegerType import IntegerType
        from prompto.param.CategoryParameter import CategoryParameter
        ITEM_ARGUMENT = CategoryParameter(IntegerType.instance, "item")
        super().__init__("removeItem", ITEM_ARGUMENT)


    def interpret(self, context):
        list = self.getValue(context)
        if not list.mutable:
            raise NotMutableError()
        item = context.getValue("item")
        list.removeItem(item)


    def check(self, context, isStart:bool):
        return VoidType.instance


class RemoveValueMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        from prompto.param.CategoryParameter import CategoryParameter
        VALUE_ARGUMENT = CategoryParameter(AnyType.instance, "value")
        super().__init__("removeValue", VALUE_ARGUMENT)


    def interpret(self, context):
        list = self.getValue(context)
        if not list.mutable:
            raise NotMutableError()
        value = context.getValue("value")
        list.removeValue(value)


    def check(self, context, isStart:bool):
        return VoidType.instance


