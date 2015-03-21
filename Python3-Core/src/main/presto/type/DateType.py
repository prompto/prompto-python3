from presto.type.AnyType import *
from presto.type.BooleanType import *
from presto.type.DateTimeType import *
from presto.type.IntegerType import *
from presto.type.NativeType import *
from presto.type.PeriodType import *
from presto.type.RangeType import *
from presto.type.TimeType import *
from presto.value.Date import *
from presto.value.DateRange import *


class DateType(NativeType):
    instance = None

    def __init__(self):
        super(DateType, self).__init__("Date")

    def isAssignableTo(self, context, other):
        return isinstance(other, DateType) or isinstance(other, AnyType)

    def checkAdd(self, context, other, tryReverse):
        if isinstance(other, PeriodType):
            return self  # ignore time section
        return super(DateType, self).checkAdd(context, other, tryReverse)

    def checkSubstract(self, context, other):
        if isinstance(other, PeriodType):
            return self  # ignore time section
        elif isinstance(other, DateType):
            return PeriodType.instance
        elif isinstance(other, TimeType):
            return PeriodType.instance
        elif isinstance(other, DateTimeType):
            return PeriodType.instance
        return super(DateType, self).checkSubstract(context, other)

    def checkCompare(self, context, other):
        if isinstance(other, DateType):
            return BooleanType.instance
        elif isinstance(other, DateTimeType):
            return BooleanType.instance
        else:
            return super(DateType, self).checkCompare(context, other)

    def checkRange(self, context, other):
        if isinstance(other, DateType):
            return RangeType(self)
        else:
            return super(DateType, self).checkRange(context, other)

    def checkMember(self, context, name):
        from presto.type.IntegerType import IntegerType
        if "year" == name:
            return IntegerType.instance
        elif "month" == name:
            return IntegerType.instance
        elif "dayOfMonth" == name:
            return IntegerType.instance
        elif "dayOfYear" == name:
            return IntegerType.instance
        else:
            return super(DateType, self).checkMember(context, name)

    def newRange(self, left, right):
        if isinstance(left, Date) and isinstance(right, Date):
            return DateRange(left, right)
        return super(DateType, self).newRange(left, right)


    def sort(self, context, source):
        return sorted(source)

    def toString(self, value):
        return "'" + value.toString() + "'"


DateType.instance = DateType()

