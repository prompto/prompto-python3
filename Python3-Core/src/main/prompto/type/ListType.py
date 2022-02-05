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
            return super().checkAdd(context, other, tryReverse)


    def checkSubstract(self, context, other):
        from prompto.type.SetType import SetType
        if isinstance(other, (ListType, SetType)) and self.itemType == other.itemType:
            return self
        else:
            return super().checkSubstract(context, other)


    def checkItem(self, context, other):
        from prompto.type.IntegerType import IntegerType
        if other == IntegerType.instance:
            return self.itemType
        else:
            return super().checkItem(context, other)


    def checkSlice(self, context):
        return self


    def checkMultiply(self, context, other, tryReverse):
        from prompto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return self
        return super().checkMultiply(context, other, tryReverse)


    def checkContainsAllOrAny(self, context, other):
        return BooleanType.instance


    def checkIterator(self, context):
        return self.itemType


    def checkMember(self, context, name):
        from prompto.type.IntegerType import IntegerType
        if "count" == name:
            return IntegerType.instance
        else:
            return super().checkMember(context, name)


    def getMemberMethods(self, context, name):
        if name == "toSet":
            return [ToSetMethodDeclaration(self.itemType)]
        elif name == "join":
            return [JoinListMethodDeclaration.getInstance()]
        elif name == "indexOf":
            return [IndexOfMethodDeclaration.getInstance()]
        elif name == "removeItem":
            return [RemoveItemMethodDeclaration.getInstance()]
        elif name == "removeValue":
            return [RemoveValueMethodDeclaration.getInstance()]
        elif name == "addValue":
            return [AddValueMethodDeclaration.getInstance()]
        elif name == "insertValue":
            return [InsertValueMethodDeclaration.getInstance()]
        else:
            return super().getMemberMethods(context, name)


    def convertPythonValueToPromptoValue(self, context, value, returnType):
        if isinstance(value, (list, set, tuple)):
            items = [self.itemType.convertPythonValueToPromptoValue(context, item, returnType) for item in value]
            from prompto.value.ListValue import ListValue
            return ListValue(self.itemType, items=items)
        else:
            return super().convertPythonValueToPromptoValue(context, value, returnType)


    def withItemType(self, itemType:IType):
        return ListType(itemType)



class JoinListMethodDeclaration(BaseJoinMethodDeclaration):

    instance = None

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = JoinListMethodDeclaration()
        return cls.instance

    def getItems(self, context):
        return self.getValue(context).items


class IndexOfMethodDeclaration(BuiltInMethodDeclaration):

    instance = None

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = IndexOfMethodDeclaration()
        return cls.instance


    def __init__(self):
        from prompto.param.CategoryParameter import CategoryParameter
        VALUE_ARGUMENT = CategoryParameter(AnyType.instance, "value")
        super().__init__("indexOf", VALUE_ARGUMENT)


    def interpret(self, context):
        list = self.getValue(context)
        value = context.getValue("value")
        return list.indexOfValue(value)


    def check(self, context):
        from prompto.type.IntegerType import IntegerType
        return IntegerType.instance


class RemoveItemMethodDeclaration(BuiltInMethodDeclaration):

    instance = None

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = RemoveItemMethodDeclaration()
        return cls.instance


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


    def check(self, context):
        return VoidType.instance


class RemoveValueMethodDeclaration(BuiltInMethodDeclaration):

    instance = None

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = RemoveValueMethodDeclaration()
        return cls.instance

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

    def check(self, context):
        return VoidType.instance


class AddValueMethodDeclaration(BuiltInMethodDeclaration):

    instance = None

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = AddValueMethodDeclaration()
        return cls.instance

    def __init__(self):
        from prompto.param.CategoryParameter import CategoryParameter
        VALUE_ARGUMENT = CategoryParameter(AnyType.instance, "value")
        super().__init__("addValue", VALUE_ARGUMENT)

    def interpret(self, context):
        list = self.getValue(context)
        if not list.mutable:
            raise NotMutableError()
        value = context.getValue("value")
        list.addValue(value)

    def check(self, context):
        return VoidType.instance

class InsertValueMethodDeclaration(BuiltInMethodDeclaration):

    instance = None

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = InsertValueMethodDeclaration()
        return cls.instance


    def __init__(self):
        from prompto.type.IntegerType import IntegerType
        from prompto.param.CategoryParameter import CategoryParameter
        VALUE_ARGUMENT = CategoryParameter(AnyType.instance, "value")
        AT_INDEX_ARGUMENT = CategoryParameter(IntegerType.instance, "atIndex")
        super().__init__("addValue", VALUE_ARGUMENT, AT_INDEX_ARGUMENT)


    def interpret(self, context):
        list = self.getValue(context)
        if not list.mutable:
            raise NotMutableError()
        value = context.getValue("value")
        atIndex = context.getValue("atIndex")
        list.insertValue(value, atIndex)


    def check(self, context):
        return VoidType.instance


class ToSetMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self, itemType):
        super().__init__("toSet")
        self.itemType = itemType

    def interpret(self, context):
        value = self.getValue(context)
        return value.toSetValue(context)

    def check(self, context):
        from prompto.type.SetType import SetType
        return SetType(self.itemType)
