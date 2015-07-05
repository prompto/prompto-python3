from prompto.error.IndexOutOfRangeError import IndexOutOfRangeError
from prompto.error.InternalError import InternalError
from prompto.type.RangeType import RangeType
from prompto.value.BaseValue import BaseValue
from prompto.value.IRange import IRange
from prompto.value.IValue import IValue
from prompto.value.Integer import Integer


class Range(BaseValue, IRange):

    def __init__(self, itemType, left, right):
        super().__init__(RangeType(itemType))
        # can't just use T extends Comparable<T> because LocalDate and LocalTime extend Comparable<R>
        if left < right:
            self.low = left
            self.high = right
        else:
            self.low = right
            self.high = left

    def __str__(self):
        return "[" + ("" if self.low is None else str(self.low)) + ".." \
               + ("" if self.high is None else str(self.high)) + "]"

    def getLow(self):
        return self.low

    def getHigh(self):
        return self.high

    def isEmpty(self):
        return self.size() == 0

    def __eq__(self, obj):
        if not isinstance(obj, Range):
            return False
        else:
            return self.low == obj.low and self.high == obj.high

    def hasItem(self, context, val):
        return not(val < self.low or val > self.high)

    def getItem(self, context, index):
        if isinstance(index, Integer):
            try:
                value = self.computeItem(index.IntegerValue())
                if isinstance(value, IValue):
                    return value
                else:
                    raise InternalError("Item not a value!")
            except IndexError:
                raise IndexOutOfRangeError()
        else:
            raise SyntaxError("No such item:" + str(index))

    def slice(self, fi, li):
        size = self.size()
        _fi = 1 if fi is None else fi.IntegerValue()
        if _fi < 1:
            raise IndexOutOfRangeError()
        _li = size if li is None else li.IntegerValue()
        if _li < 1:
            _li = size + 1 + _li;
        elif _li > size:
            raise IndexOutOfRangeError()
        return self.newInstance(self.computeItem(_fi), self.computeItem(_li))

    def getItems(self, context):
        size = self.size()
        index = 1
        while index <= size:
            yield self.getItem(context, Integer(index))
            index += 1
