from prompto.type.AnyType import *
from prompto.type.BooleanType import *
from prompto.type.ListType import *
from prompto.type.NativeType import *


class TupleType(NativeType):
    instance = None

    def __init__(self):
        super(TupleType, self).__init__("Tuple")

    def isAssignableTo(self, context, other):
        return isinstance(other, TupleType) or isinstance(other, AnyType)

    def checkItem(self, context, other):
        from prompto.type.IntegerType import IntegerType
        if other == IntegerType.instance:
            return AnyType.instance
        else:
            return super(TupleType, self).checkItem(context, other)

    def checkMember(self, context, name):
        from prompto.type.IntegerType import IntegerType
        if "length" == name:
            return IntegerType.instance
        else:
            return super(TupleType, self).checkMember(context, name)

    def checkAdd(self, context, other, tryReverse):
        if isinstance(other, TupleType) or isinstance(other, ListType):
            return self
        else:
            return super(TupleType, self).checkAdd(context, other, tryReverse)

    def checkContains(self, context, other):
        return BooleanType.instance

    def checkContainsAllOrAny(self, context, other):
        return BooleanType.instance


TupleType.instance = TupleType()

