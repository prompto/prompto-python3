from presto.error.IndexOutOfRangeError import IndexOutOfRangeError
from presto.value.Period import Period
from presto.value.Range import Range


class DateRange(Range):

    def __init__(self, left, right):
        from presto.type.DateType import DateType
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
        result = self.low.plus(Period(days=index - 1))
        if result < self.low or result > self.high:
            raise IndexOutOfRangeError()
        return result

    def newInstance(self, left, right):
        return DateRange(left, right)
