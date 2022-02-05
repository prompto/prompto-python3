from prompto.declaration.BuiltInMethodDeclaration import BuiltInMethodDeclaration
from prompto.error.NotMutableError import NotMutableError
from prompto.type.AnyType import AnyType
from prompto.type.BooleanType import BooleanType
from prompto.type.ContainerType import ContainerType
from prompto.type.EntryType import EntryType
from prompto.type.IType import IType
from prompto.type.IntegerType import IntegerType
from prompto.type.ListType import ListType
from prompto.type.SetType import SetType
from prompto.type.TextType import TextType
from prompto.store.TypeFamily import TypeFamily
from prompto.type.VoidType import VoidType


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


    def getMemberMethods(self, context, name):
        if name == "swap":
            return [SwapMethodDeclaration()]
        elif name == "removeKey":
            return [RemoveKeyMethodDeclaration()]
        elif name == "removeValue":
            return [RemoveValueMethodDeclaration()]
        else:
            return super().getMemberMethods(context, name)


    def withItemType(self, itemType:IType):
        return DictType(itemType)


class SwapMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        super().__init__("swap")


    def interpret(self, context):
        value = self.getValue(context)
        return value.swap(context)


    def check(self, context):
        return DictType(TextType.instance)


class RemoveKeyMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        from prompto.param.CategoryParameter import CategoryParameter
        KEY_ARGUMENT = CategoryParameter(TextType.instance, "key")
        super().__init__("removeKey", KEY_ARGUMENT)


    def interpret(self, context):
        dict = self.getValue(context)
        if not dict.mutable:
            raise NotMutableError()
        key = context.getValue("key")
        dict.removeKey(key)


    def check(self, context):
        return VoidType.instance


class RemoveValueMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        from prompto.param.CategoryParameter import CategoryParameter
        VALUE_ARGUMENT = CategoryParameter(AnyType.instance, "value")
        super().__init__("removeValue", VALUE_ARGUMENT)


    def interpret(self, context):
        dict = self.getValue(context)
        if not dict.mutable:
            raise NotMutableError()
        value = context.getValue("value")
        dict.removeValue(value)


    def check(self, context):
        return VoidType.instance
