from io import StringIO
from prompto.type.PeriodType import PeriodType
from prompto.value.BaseValue import BaseValue
from prompto.value.IMultiplyable import IMultiplyable
from prompto.value.Integer import Integer

class Period ( BaseValue, IMultiplyable ):

    ZERO = None
    
    @staticmethod 
    def Parse(text):
        try:
            data = [0]*8
            steps = "YMWDHM.S"
            value = None
            lastStep = -1
            isNeg = False
            inPeriod = False
            inTime = False
            inMillis = False

            for c in text:
                # leading 'P' is mandatory
                if not inPeriod:
                    if c == 'P':
                        inPeriod = True
                        continue
                    else:
                        raise Exception()
                # check for time section
                if c == 'T':
                    if not inTime:
                        inTime = True
                        continue
                    else:
                        raise Exception()
                # check for value type
                step = steps.find(c, 4) if inTime else steps.find(c)
                if step >= 0:
                    if step <= lastStep:
                        raise Exception()
                    if step > 3 and not inTime:
                        raise Exception()
                    if value == None:
                        raise Exception()
                    if step == 6: # millis '.'
                        inMillis = True
                    if step == 7 and not inMillis:
                        step = 6
                    data[step] = value
                    lastStep = step
                    value = None
                    continue
                if c == '-':
                    if value is not None:
                        raise Exception()
                    if isNeg or inMillis:
                        raise Exception()
                    isNeg = True
                if c < '0' or c > '9':
                    raise Exception()
                if value is not None:
                    value *= 10
                    value += ord(c) - ord('0')
                else:
                    value = ord(c) - ord('0')
                    if isNeg:
                        value = -value
                        isNeg = False
            # must terminate by a value type
            if value is not None:
                raise Exception()
            return Period(years=data[0], months=data[1], weeks=data[2], days=data[3],
                          hours=data[4], minutes=data[5], seconds=data[6], millis=data[7])
        except Exception as e:
            from prompto.error.InvalidDataError import InvalidDataError
            raise InvalidDataError("\"" + text + "\" is not a valid ISO 8601 period!")
 
    def __init__(self, years = 0, months = 0, weeks = 0, days = 0,
                 hours = 0, minutes = 0, seconds = 0, millis = 0, delta=None):
        super().__init__(PeriodType.instance)
        if delta is not None:
            millis = delta.microseconds / 1000
            total = delta.total_seconds()
            seconds = total % 60
            total = int(total / 60)
            minutes = total % 60
            total = int(total / 60)
            hours = total % 24
            total = int(total / 24)
            days = total
            weeks = 0
            months = 0
            years = 0
        self.years = years
        self.months = months
        self.weeks = weeks
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.millis = millis

    def Add(self, context, value):
        if isinstance(value, Period):
            return self.plus(value)
        else:
            raise SyntaxError("Illegal: Period + " + type(value).__name__)
 
    def Subtract(self, context, value):
        if isinstance(value, Period):
            return self.minus(value)
        else:
            raise SyntaxError("Illegal: Period - " + type(value).__name__)
    
    def Multiply(self, context, value):
        if isinstance(value, Integer):
            count = value.IntegerValue()
            if count < 0:
                raise SyntaxError("Negative repeat count:" + count)
            elif count == 0:
                return Period.ZERO
            elif count == 1:
                return self
            else:
                return self.times(count)
        else:
            raise SyntaxError("Illegal: Period * " + type(value).__name__)
        
    def ConvertTo(self, type_):
        return self
 
    def plus(self, period):
        millis = self.millis + period.millis
        seconds = int(millis/1000)
        millis %= 1000
        return Period(self.years + period.years,
                        self.months + period.months,
                        self.weeks + period.weeks,
                        self.days + period.days,
                        self.hours + period.hours,
                        self.minutes + period.minutes,
                        self.seconds + period.seconds + seconds,
                        millis)

    def minus(self, period):
        days = self.days - period.days
        hours = self.hours - period.hours
        minutes = self.minutes - period.minutes
        seconds = self.seconds - period.seconds
        millis = self.millis - period.millis
        if millis < 0:
            seconds += int((millis - 999)/1000)
            millis = abs( millis % 1000)
        if seconds < 0:
            minutes += int((seconds - 59)/60)
            seconds = abs (seconds % 60)
        if minutes < 0:
            hours += int((minutes - 59)/60)
            minutes = abs (minutes % 60)
        if hours < 0:
            days += int((hours - 23)/24)
            hours = abs (hours % 24)
        return Period(self.years - period.years,
                        self.months - period.months,
                        self.weeks - period.weeks,
                        days, hours, minutes, seconds, millis)

    def inverse(self):
        return Period(-self.years, -self.months, -self.weeks, -self.days,
                        -self.hours, -self.minutes, -self.seconds, -self.millis)

    def times(self, count):
        return Period(self.years * count,
                        self.months * count,
                        self.weeks * count,
                        self.days * count,
                        self.hours * count,
                        self.minutes * count,
                        self.seconds * count,
                        self.millis * count)

    def __str__(self):
        s = StringIO()
        try:
            s.write("P")
            if self.years!=0:
                s.write(str(self.years))
                s.write("Y")
            if self.months!=0:
                s.write(str(self.months))
                s.write("M")
            if self.weeks!=0:
                s.write(str(self.weeks))
                s.write("W")
            if self.days!=0:
                s.write(str(self.days))
                s.write("D")
            if self.hours!=0 or self.minutes!=0 or self.seconds!=0 or self.millis!=0:
                s.write("T")
            if self.hours!=0:
                s.write(str(self.hours))
                s.write("H")
            if self.minutes!=0:
                s.write(str(self.minutes))
                s.write("M")
            if self.seconds!=0 or self.millis!=0:
                s.write(str(self.seconds))
                if self.millis!=0:
                    s.write(".")
                    s.write(str(self.millis).zfill(3))
                s.write("S")
            return s.getvalue()
        finally:
            s.close()

    def __eq__(self, obj):
        if isinstance(obj, Period):
            return self.years==obj.years \
                and self.months==obj.months \
                and self.weeks==obj.weeks \
                and self.days==obj.days \
                and self.hours==obj.hours \
                and self.minutes==obj.minutes \
                and self.seconds==obj.seconds \
                and self.millis==obj.millis
        else:
            return False
 
Period.ZERO = Period(0, 0, 0, 0, 0, 0, 0, 0)


