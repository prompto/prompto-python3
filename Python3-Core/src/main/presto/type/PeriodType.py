from presto.type.BooleanType import *
from presto.type.NativeType import *


class PeriodType(NativeType):
    instance = None

    def __init__(self):
        super(PeriodType, self).__init__("Duration")

    def isAssignableTo(self, context, other):
        return isinstance(other, PeriodType) or isinstance(other, AnyType)

    def checkAdd(self, context, other, tryReverse):
        if isinstance(other, PeriodType):
            return self
        else:
            return super(PeriodType, self).checkAdd(context, other, tryReverse)

    def checkSubstract(self, context, other):
        if isinstance(other, PeriodType):
            return self
        else:
            return super(PeriodType, self).checkSubstract(context, other)

    def checkMultiply(self, context, other, tryReverse):
        from presto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return self
        else:
            return super(PeriodType, self).checkMultiply(context, other, tryReverse)

    def checkCompare(self, context, other):
        if isinstance(other, PeriodType):
            return BooleanType.instance
        else:
            return super(PeriodType, self).checkCompare(context, other)


PeriodType.instance = PeriodType()

