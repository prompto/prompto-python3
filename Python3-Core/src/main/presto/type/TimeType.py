from presto.type.AnyType import *
from presto.type.BooleanType import *
from presto.type.DateTimeType import *
from presto.type.IntegerType import *
from presto.type.NativeType import *
from presto.type.PeriodType import *
from presto.type.RangeType import *
from presto.value.Time import *
from presto.value.TimeRange import *


class TimeType(NativeType):
    instance = None

    def __init__(self):
        super(TimeType, self).__init__("Time")

    def isAssignableTo(self, context, other):
        return isinstance(other, TimeType) or isinstance(other, AnyType)

    def checkAdd(self, context, other, tryReverse):
        from presto.type.DateTimeType import DateTimeType
        if isinstance(other, PeriodType):
            return DateTimeType.instance
        else:
            return super(TimeType, self).checkAdd(context, other, tryReverse)

    def checkSubstract(self, context, other):
        if isinstance(other, TimeType):
            return PeriodType.instance
        elif isinstance(other, PeriodType):
            return DateTimeType.instance
        else:
            return super(TimeType, self).checkSubstract(context, other)

    def checkCompare(self, context, other):
        if isinstance(other, TimeType):
            return BooleanType.instance
        else:
            return super(TimeType, self).checkCompare(context, other)

    def checkRange(self, context, other):
        if isinstance(other, TimeType):
            return RangeType(self)
        else:
            return super(TimeType, self).checkRange(context, other)

    def checkMember(self, context, name):
        from presto.type.IntegerType import IntegerType
        if "hour" == name:
            return IntegerType.instance
        elif "minute" == name:
            return IntegerType.instance
        elif "second" == name:
            return IntegerType.instance
        elif "millis" == name:
            return IntegerType.instance
        else:
            return super(TimeType, self).checkMember(context, name)

    def newRange(self, left, right):
        if isinstance(left, Time) and isinstance(right, Time):
            return TimeRange(left, right)
        else:
            return super(TimeType, self).newRange(left, right)

    def sort(self, context, source):
        return sorted(source)

    def toString(self, value):
        return "'" + str(value) + "'"


TimeType.instance = TimeType()
