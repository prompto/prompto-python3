from datetime import date, datetime, timedelta

from prompto.value.BaseValue import BaseValue
from prompto.value.IntegerValue import IntegerValue
from prompto.value.PeriodValue import PeriodValue
from prompto.error.SyntaxError import SyntaxError

class DateValue (BaseValue):

    @staticmethod
    def Parse(text):
        years = int(text[0:4])
        months = int(text[5:7])
        days = int(text[8:10])
        return DateValue(years=years, months=months, days=days)

    def __init__(self, value=None, years=None, months=None, days=None):
        from prompto.type.DateType import DateType
        super().__init__(DateType.instance)
        if value is None:
            value = date(years, months, days)
        self.value = value

    def getValue(self):
        return self.value

    def Add(self, context, value):
        if isinstance(value, PeriodValue):
            return self.plus(value)
        else:
            raise SyntaxError("Illegal: Date + " + type(value).__name__)
 
    def Subtract(self, context, value):
        if isinstance(value, DateValue):
            td = self.value - value.value
            return PeriodValue(delta=td)
        elif isinstance(value, PeriodValue):
            return self.minus(value)
        else:
            raise SyntaxError("Illegal: Date - " + type(value).__name__)

    def compareTo(self, context, value):
        if isinstance(value, DateValue):
            if self.value < value.value:
                return -1
            elif self.value == value.value:
                return 0
            else:
                return 1
        else:
            raise SyntaxError("Illegal comparison: Date - " + type(value).__name__)

    def getMemberValue(self, context, name, autoCreate=False):
        if "year"==name:
            return IntegerValue(self.value.year)
        elif "month"==name:
            return IntegerValue(self.value.month)
        elif "dayOfMonth"==name:
            return IntegerValue(self.value.day)
        elif "dayOfYear"==name:
            day = 1 + self.value.toordinal() - date(self.value.year,1,1).toordinal()
            return IntegerValue(day)
        else:
            return super().getMemberValue(context, name, autoCreate)
 
    def ConvertTo(self, itype):
        return self.value
    
    def toDateMidnight(self):
        return self

    def minus(self, period):
        dt = datetime(self.value.year, self.value.month, self.value.day)
        td = timedelta(weeks=period.weeks, days=period.days)
        month = self.value.month - period.months
        year = self.value.year - period.years - int(month / 12)
        month %= 12
        value = dt.replace(year=year, month=month) - td
        return DateValue(value.date())

    def plus(self, period):
        dt = datetime(self.value.year, self.value.month, self.value.day)
        td = timedelta(weeks=period.weeks, days=period.days)
        month = self.value.month + period.months
        year = self.value.year + period.years + int(month / 12)
        month %= 12
        value = dt.replace(year=year, month=month) + td
        return DateValue(value.date())

    def __eq__(self, obj):
        if isinstance(obj, DateValue):
            return self.value == obj.value
        else:
            return self.value == obj

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return self.value.isoformat()

    def __hash__(self):
        return hash(self.value)
