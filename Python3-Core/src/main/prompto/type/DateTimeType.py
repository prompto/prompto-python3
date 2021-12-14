from datetime import datetime

from prompto.type.DateType import DateType
from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily
from prompto.type.TimeType import TimeType


class DateTimeType(NativeType):
    instance = None

    def __init__(self):
        super(DateTimeType, self).__init__(TypeFamily.DATETIME)
        self.typeName = "DateTime"

    def convertPythonValueToPromptoValue(self, context, value, returnType):
        if isinstance(value, datetime):
            from prompto.value.DateTimeValue import DateTimeValue
            return DateTimeValue(value)
        else:
            return super().convertPythonValueToPromptoValue(context, value, returnType)  # TODO for now


    def checkAdd(self, context, other, tryReverse):
        from prompto.type.PeriodType import PeriodType
        if isinstance(other, PeriodType):
            return self
        else:
            return super(DateTimeType, self).checkAdd(context, other, tryReverse)


    def checkSubstract(self, context, other):
        from prompto.type.PeriodType import PeriodType
        if isinstance(other, DateTimeType):
            return PeriodType.instance
        elif isinstance(other, PeriodType):
            return self
        else:
            return super(DateTimeType, self).checkSubstract(context, other)


    def checkCompare(self, context, other):
        from prompto.type.BooleanType import BooleanType
        from prompto.type.DateType import DateType
        if isinstance(other, DateType):
            return BooleanType.instance
        elif isinstance(other, DateTimeType):
            return BooleanType.instance
        else:
            return super(DateTimeType, self).checkCompare(context, other)


    def checkMember(self, context, name):
        from prompto.type.IntegerType import IntegerType
        from prompto.type.TextType import TextType
        if "year" == name:
            return IntegerType.instance
        elif "month" == name:
            return IntegerType.instance
        elif "dayOfMonth" == name:
            return IntegerType.instance
        elif "dayOfYear" == name:
            return IntegerType.instance
        elif "hour" == name:
            return IntegerType.instance
        elif "minute" == name:
            return IntegerType.instance
        elif "second" == name:
            return IntegerType.instance
        elif "millisecond" == name:
            return IntegerType.instance
        elif "tzOffset" == name:
            return IntegerType.instance
        elif "tzName" == name:
            return TextType.instance
        elif "date" == name:
            return DateType.instance
        elif "time" == name:
            return TimeType.instance
        else:
            return super(DateTimeType, self).checkMember(context, name)


    def toString(self, value):
        return "'" + str(value) + "'"


DateTimeType.instance = DateTimeType()
