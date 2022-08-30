from prompto.declaration.BuiltInMethodDeclaration import BuiltInMethodDeclaration
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


    def getMemberMethods(self, context, name):
        if name == "toList":
            return [ToListMethodDeclaration(self.itemType)]
        elif name == "toSet":
            return [ToSetMethodDeclaration(self.itemType)]
        else:
            return super().getMemberMethods(context, name)


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
