from prompto.type.AnyType import AnyType
from prompto.type.BooleanType import BooleanType
from prompto.type.ContainerType import BaseJoinMethodDeclaration
from prompto.type.IType import IType
from prompto.type.ListType import ListType
from prompto.type.SetType import SetType
from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily



class TupleType(NativeType):
    instance = None

    def __init__(self):
        super().__init__(TypeFamily.TUPLE)


    def isAssignableFrom(self, context, other):
        return super().isAssignableFrom(context, other) or \
               isinstance(other, (ListType, SetType))


    def checkItem(self, context, other):
        from prompto.type.IntegerType import IntegerType
        if other == IntegerType.instance:
            return AnyType.instance
        else:
            return super().checkItem(context, other)


    def checkMember(self, context, name):
        from prompto.type.IntegerType import IntegerType
        if "count" == name:
            return IntegerType.instance
        else:
            return super().checkMember(context, name)


    def checkAdd(self, context, other, tryReverse):
        if isinstance(other, (TupleType, ListType, SetType)):
            return self
        else:
            return super().checkAdd(context, other, tryReverse)


    def checkContains(self, context, other):
        return BooleanType.instance


    def checkContainsAllOrAny(self, context, other):
        return BooleanType.instance


    def getMemberMethods(self, context, name):
        if name == "join":
            return [JoinTupleMethodDeclaration()]
        else:
            return super().getMemberMethods(context, name)


    def withItemType(self, itemType:IType):
        return self


TupleType.instance = TupleType()

class JoinTupleMethodDeclaration(BaseJoinMethodDeclaration):

    def getItems(self, context):
        return self.getValue(context).items
