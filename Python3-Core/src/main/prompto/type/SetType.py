from prompto.declaration.BuiltInMethodDeclaration import BuiltInMethodDeclaration
from prompto.type.BooleanType import BooleanType
from prompto.type.ContainerType import ContainerType, BaseJoinMethodDeclaration
from prompto.store.TypeFamily import TypeFamily
from prompto.type.IType import IType


class SetType(ContainerType):

    def __init__(self, itemType):
        super().__init__(TypeFamily.SET, itemType)
        self.typeName = itemType.typeName + "<>"


    def isAssignableFrom(self, context, other):
        return super().isAssignableFrom(context, other) or \
               (isinstance(other, SetType) and self.itemType.isAssignableFrom(context, other.itemType))


    def __eq__(self, obj):
        if id(obj) == id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, SetType):
            return False
        return self.itemType == obj.itemType


    def checkAdd(self, context, other, tryReverse):
        from prompto.type.ListType import ListType
        if isinstance(other, (ListType, SetType)) and self.itemType.isAssignableFrom(context, other.itemType):
            return self
        else:
            return super().checkAdd(context, other, tryReverse)


    def checkSubstract(self, context, other):
        from prompto.type.ListType import ListType
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
        if name == "toList":
            return [ToListMethodDeclaration(self.itemType)]
        elif name == "join":
            return [JoinSetMethodDeclaration.getInstance()]
        else:
            return super().getMemberMethods(context, name)


    def withItemType(self, itemType:IType):
        return SetType(itemType)


class JoinSetMethodDeclaration(BaseJoinMethodDeclaration):

    instance = None

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = JoinSetMethodDeclaration()
        return cls.instance

    def getItems(self, context):
        return self.getValue(context).items


class ToListMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self, itemType):
        super().__init__("toList")
        self.itemType = itemType


    def interpret(self, context):
        value = self.getValue(context)
        return value.toListValue(context)


    def check(self, context):
        from prompto.type.ListType import ListType
        return ListType(self.itemType, False)

