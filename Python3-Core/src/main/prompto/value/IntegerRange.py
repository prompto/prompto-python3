from prompto.error.IndexOutOfRangeError import IndexOutOfRangeError
from prompto.value.IntegerValue import IntegerValue
from prompto.value.RangeValue import RangeValue


class IntegerRange (RangeValue):

    def __init__(self, left, right):
        from prompto.type.IntegerType import IntegerType
        super(IntegerRange, self).__init__(IntegerType.instance, left, right)

    def size(self):
        return 1 + self.high.IntegerValue() - self.low.IntegerValue()

    def compare(self, o1,  o2):
        if o1.value < o2.value:
            return -1
        elif o1.value == o2.value:
            return 0
        else:
            return 1

    def computeItem(self, index):
        result = self.low.IntegerValue() + index - 1
        if result>self.high.IntegerValue():
            raise IndexOutOfRangeError()
        return IntegerValue(result)

    def newInstance(self, left, right):
        return IntegerRange(left, right)
