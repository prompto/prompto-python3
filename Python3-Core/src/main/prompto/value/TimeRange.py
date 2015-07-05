from prompto.error.IndexOutOfRangeError import IndexOutOfRangeError
from prompto.value.Range import Range
from prompto.value.Period import Period


class TimeRange(Range):

    def __init__(self, left, right):
        from prompto.type.TimeType import TimeType
        super(TimeRange, self).__init__(TimeType.instance, left, right)

    def size(self):
        return 1 + (self.high.getMillisOfDay() - self.low.getMillisOfDay()) / 1000

    def compare(self, o1, o2):
        if o1.value < o2.value:
            return -1
        elif o1.value == o2.value:
            return 0
        else:
            return 1

    def computeItem(self, index):
        result = self.low.plus(Period(seconds=index - 1))
        if result<self.low or result>self.high:
            raise IndexOutOfRangeError()
        return result

    def newInstance(self, left, right):
        return TimeRange(left, right)
