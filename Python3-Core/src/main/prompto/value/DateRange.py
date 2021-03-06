from prompto.error.IndexOutOfRangeError import IndexOutOfRangeError
from prompto.value.PeriodValue import PeriodValue
from prompto.value.RangeValue import RangeValue


class DateRange(RangeValue):

    def __init__(self, left, right):
        from prompto.type.DateType import DateType
        super(DateRange, self).__init__(DateType.instance, left, right)

    def size(self):
        h = self.high.getValue().toordinal()
        l = self.low.getValue().toordinal()
        return 1 + h - l

    def compare(self, o1, o2):
        if o1.value < o2.value:
            return -1
        elif o1.value == o2.value:
            return 0
        else:
            return 1

    def computeItem(self, index):
        result = self.low.plusPeriod(PeriodValue(days=index - 1))
        if result < self.low or result > self.high:
            raise IndexOutOfRangeError()
        return result

    def newInstance(self, left, right):
        return DateRange(left, right)
