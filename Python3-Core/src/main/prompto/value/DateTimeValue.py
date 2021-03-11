from datetime import date, datetime, timedelta

from prompto.error.SyntaxError import SyntaxError
from prompto.value.BaseValue import BaseValue


class DateTimeValue(BaseValue):

    def __init__(self, value=None, year=None, month=None, day=None, hour=None, minute=None, second=None, millis=None):
        from prompto.type.DateTimeType import DateTimeType
        super().__init__(DateTimeType.instance)
        if value is None:
            value = datetime(year, month, day, hour, minute, second, millis)
        self.value = value


    def getValue(self):
        return self.value


    def convertToPython(self):
        return self.value


    def Add(self, context, value):
        from prompto.value.PeriodValue import PeriodValue
        if isinstance(value, PeriodValue):
            return self.plus(value)
        else:
            raise SyntaxError("Illegal: DateTime + " + type(value).__name__)


    def Subtract(self, context, value):
        from prompto.value.PeriodValue import PeriodValue
        if isinstance(value, DateTimeValue):
            td = self.value - value.value
            return PeriodValue(delta=td)
        elif isinstance(value, PeriodValue):
            return self.minus(value)
        else:
            raise SyntaxError("Illegal: DateTime - " + type(value).__name__)


    def compareTo(self, context, value):
        if isinstance(value, DateTimeValue):
            if self.value < value.value:
                return -1
            elif self.value == value.value:
                return 0
            else:
                return 1
        else:
            raise SyntaxError("Illegal comparison: DateTime + " + type(value).__name__)


    def getMemberValue(self, context, name, autoCreate=False):
        from prompto.value.IntegerValue import IntegerValue
        if "year" == name:
            return IntegerValue(self.value.year)
        elif "month" == name:
            return IntegerValue(self.value.month)
        elif "dayOfMonth" == name:
            return IntegerValue(self.value.day)
        elif "dayOfYear" == name:
            day = 1 + self.value.toordinal() - date(self.value.year, 1, 1).toordinal()
            return IntegerValue(day)
        elif "hour" == name:
            return IntegerValue(self.value.hour)
        elif "minute" == name:
            return IntegerValue(self.value.minute)
        elif "second" == name:
            return IntegerValue(self.value.second)
        elif "millisecond" == name:
            return IntegerValue(self.value.microsecond // 1000)
        elif "tzOffset" == name:
            return IntegerValue(0)  # self.value.getZone().toTimeZone().getRawOffset() / 1000)
        elif "tzName" == name:
            from prompto.value.TextValue import TextValue
            return TextValue("Z")  # self.value.getZone().toTimeZone().getDisplayName())
        elif "date" == name:
            from prompto.value.DateValue import DateValue
            return DateValue(years=self.value.year, months=self.value.month, days=self.value.day)
        elif "time" == name:
            from prompto.value.TimeValue import TimeValue
            return TimeValue(hours=self.value.hour, minutes=self.value.minute, seconds=self.value.second, millis=self.value.microsecond // 1000)
        else:
            return super().getMemberValue(context, name, autoCreate)


    def plus(self, period):
        td = timedelta(weeks=period.weeks, days=period.days, hours=period.hours, minutes=period.minutes,
                       seconds=period.seconds, milliseconds=period.millis)
        year = self.value.year + period.years
        if period.months != 0:
            month = self.value.month + period.months
            year += int(month / 12)
            month %= 12
        else:
            month = self.value.month
        value = self.value.replace(year=year, month=month) + td
        return DateTimeValue(value)


    def minus(self, period):
        td = timedelta(weeks=period.weeks, days=period.days, hours=period.hours, minutes=period.minutes,
                       seconds=period.seconds, milliseconds=period.millis)
        year = self.value.year - period.years
        if period.months != 0:
            month = self.value.month - period.months
            month %= 12
            year -= int(month / 12)
        else:
            month = self.value.month
        value = self.value.replace(year=year, month=month) - td
        return DateTimeValue(value)


    def ConvertTo(self, itype):
        return self.value


    def __lt__(self, obj):
        return self.value < obj.value

    def __eq__(self, obj):
        if isinstance(obj, DateTimeValue):
            return self.value == obj.value
        else:
            return self.value == obj


    def __str__(self):
        s = self.value.isoformat()
        if self.value.microsecond == 0:
            s = s[0:19] + ".000" + s[19:]
        else:
            s = s[0:23] + s[26:]
        if self.value.tzinfo is None:
            s = s + "Z"
        return s


    def __hash__(self):
        return hash(self.value)


    @staticmethod
    def Parse(text):
        year = int(text[0:4])
        text = text[5:]
        month = int(text[0:2])
        text = text[3:]
        day = int(text[0:2])
        text = text[3:]
        if len(text) > 0:
            hour = int(text[0:2])
            text = text[3:]
        else:
            hour = 0
        if len(text) > 0:
            minute = int(text[0:2])
            text = text[3:]
        else:
            minute = 0
        if len(text) > 0:
            second = int(text[0:2])
            text = text[2:]
        else:
            second = 0
        if len(text) > 0 and text[0] == '.':
            text = text[1:]
            buffer = ""
            while len(text) > 0 and text[0] >= '0' and text[0] <= '9':
                buffer += text[0]
                text = text[1:]
            while len(buffer) < 6:
                buffer += '0'
            micro = int(buffer)
        else:
            micro = 0
        zone = None
        dt = datetime(year, month, day, hour, minute, second, micro, zone)
        return DateTimeValue(value=dt)


    def toDocumentValue(self, context):
        from prompto.value.TextValue import TextValue
        return TextValue(str(self))


    def toJsonNode(self):
        return str(self)
