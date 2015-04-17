from presto.value.BaseValue import BaseValue
from presto.value.ISliceable import ISliceable
from presto.value.Integer import Integer
from presto.value.IValue import IValue
from presto.expression.IExpression import IExpression
from presto.error.IndexOutOfRangeError import IndexOutOfRangeError
from presto.error.InternalError import InternalError


class BaseValueList(BaseValue, ISliceable):

    def __init__(self, type, items=None):
        super().__init__(type)
        if items is None:
            items = []
        self.items = items

    def __str__(self):
        return str(self.items)

    def getItems(self, context=None):
        for item in self.items:
            yield item

    def append(self, o):
        self.items.append(o)

    def extend(self, items):
        self.items.extend(items)

    def get(self, index):
        return self.items[index]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def slice(self, fi, li):
        _fi = 1 if fi is None else fi.IntegerValue()
        if _fi < 0:
            raise IndexOutOfRangeError()
        _li = len(self.items) if li is None else li.IntegerValue()
        if _li < 0:
            _li = len(self.items) + 1 + _li
        if _li > len(self.items):
            raise IndexOutOfRangeError()
        return self.newInstance(self.items[_fi-1:_li]) # 0 based, right limit excluded

    def merge(self, other):
        result = []
        result.extend(self.items)
        result.extend(other.items)
        return self.newInstance(result)

    def hasItem(self, context, lval):
        for item in self.items:
            if item == lval:
                return True
        return False

    def getItem(self, context, index):
        if isinstance(index, Integer):
            try:
                idx = index.IntegerValue() - 1
                return self.items[idx]
            except IndexError:
                raise IndexOutOfRangeError()
        else:
            raise SyntaxError("No such item:" + index.toString())

    def __eq__(self, obj):
        if not isinstance(obj, BaseValueList):
            return False
        return self.items == obj.items

    def GetMember(self, context, name):
        if "length" == name:
            return Integer(len(self.items))
        else:
            return super(BaseValueList, self).GetMember(context, name)

