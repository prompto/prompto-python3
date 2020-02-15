from datetime import time, datetime, timedelta

from prompto.value.BaseValue import BaseValue
from prompto.value.IntegerValue import IntegerValue
from prompto.value.PeriodValue import PeriodValue
from prompto.error.SyntaxError import SyntaxError

class TimeValue(BaseValue):

    @staticmethod
    def Parse(text):
        hours = int(text[0:2])
        minutes = int(text[3:5])
        if len(text) > 6:
            seconds = int(text[6:8])
        else:
            seconds = 0
        if len(text) > 8 and text[8] == '.':
            millis = int(text[9:])
        else:
            millis = 0
        return TimeValue(time(hours, minutes, seconds, millis * 1000))

    def __init__(self, value=None, hours=None, minutes=None, seconds=None, millis=0):
        from prompto.type.TimeType import TimeType
        super(TimeValue, self).__init__(TimeType.instance)
        if value is None:
            value = time(hours, minutes, seconds, millis*1000)
        self.value = value

    def getValue(self):
        return self.value

    def Add(self, context, value):
        if isinstance(value, PeriodValue):
            return self.plus(value)
        else:
            raise SyntaxError("Illegal: Time + " + type(value).__name__)

    def Subtract(self, context, value):
        if isinstance(value, TimeValue):
            return PeriodValue(hours=self.value.hour - value.value.hour, \
                               minutes=self.value.minute - value.value.minute, \
                               seconds=self.value.second - value.value.second, \
                               millis=(self.value.microsecond - value.value.microsecond)/1000)
        elif isinstance(value, PeriodValue):
            return self.minus(value)
        else:
            raise SyntaxError("Illegal: Time - " + type(value).__name__)


    def compareTo(self, context, value):
        if isinstance(value, TimeValue):
            if self.value < value.value:
                return -1
            elif self.value == value.value:
                return 0
            else:
                return 1
        else:
            raise SyntaxError("Illegal comparison: Time + " + type(value).__name__)


    def getMemberValue(self, context, name, autoCreate=False):
        if "hour" == name:
            return IntegerValue(self.value.hour)
        elif "minute" == name:
            return IntegerValue(self.value.minute)
        elif "second" == name:
            return IntegerValue(self.value.second)
        elif "millisecond" == name:
            return IntegerValue(self.value.microsecond // 1000)
        else:
            return super().getMemberValue(context, name, autoCreate)


    def ConvertTo(self, itype):
        return self.value


    def minus(self, period):
        dt = datetime(2000,1,1,hour=self.value.hour, minute=self.value.minute, second=self.value.second, microsecond=self.value.microsecond)
        td = timedelta(hours=period.hours,minutes=period.minutes,seconds=period.seconds,milliseconds=period.millis)
        value = dt - td
        return TimeValue(value.time())

    def plus(self, period):
        dt = datetime(2000,1,1,hour=self.value.hour, minute=self.value.minute, second=self.value.second, microsecond=self.value.microsecond)
        td = timedelta(hours=period.hours,minutes=period.minutes,seconds=period.seconds,milliseconds=period.millis)
        value = dt + td
        return TimeValue(value.time())


    def getMillisOfDay(self):
        return (self.value.microsecond / 1000) + \
               (self.value.second * 1000) + \
               (self.value.minute * 60 * 1000) + \
               (self.value.hour * 60 * 60 * 1000)

    def __lt__(self, other):
        return self.value < other.value


    def __eq__(self, obj):
        if isinstance(obj, TimeValue):
            return self.value == obj.value
        else:
            return self.value == obj

    def __str__(self):
        s = self.value.isoformat()
        if self.value.microsecond==0:
            s = s[0:8] + ".000"
        else:
            s = s[0:12]
        return s

    def __hash__(self):
        return hash(self.value)
