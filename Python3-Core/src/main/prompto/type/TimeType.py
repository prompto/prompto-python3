from prompto.type.AnyType import *
from prompto.type.BooleanType import *
from prompto.type.DateTimeType import *
from prompto.type.IntegerType import *
from prompto.type.NativeType import *
from prompto.type.PeriodType import *
from prompto.type.RangeType import *
from prompto.value.Time import *
from prompto.value.TimeRange import *


class TimeType(NativeType):
    instance = None

    def __init__(self):
        super(TimeType, self).__init__(TypeFamily.TIME)

    def isAssignableFrom(self, context, other):
        return super().isAssignableFrom(context, other) or \
            other is DateTimeType.instance

    def checkAdd(self, context, other, tryReverse):
        from prompto.type.DateTimeType import DateTimeType
        if isinstance(other, PeriodType):
            return DateTimeType.instance
        else:
            return super(TimeType, self).checkAdd(context, other, tryReverse)

    def checkSubstract(self, context, other):
        if isinstance(other, TimeType):
            return PeriodType.instance
        elif isinstance(other, PeriodType):
            return self
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
        from prompto.type.IntegerType import IntegerType
        if "hour" == name:
            return IntegerType.instance
        elif "minute" == name:
            return IntegerType.instance
        elif "second" == name:
            return IntegerType.instance
        elif "millisecond" == name:
            return IntegerType.instance
        else:
            return super(TimeType, self).checkMember(context, name)

    def newRange(self, left, right):
        if isinstance(left, Time) and isinstance(right, Time):
            return TimeRange(left, right)
        else:
            return super(TimeType, self).newRange(left, right)

    def sort(self, context, source, desc):
        return sorted(source, reverse=desc)

    def toString(self, value):
        return "'" + str(value) + "'"


TimeType.instance = TimeType()
