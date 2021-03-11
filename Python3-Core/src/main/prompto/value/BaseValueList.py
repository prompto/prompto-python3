from prompto.type.NativeType import NativeType
from prompto.value.BaseValue import BaseValue
from prompto.value.ISliceable import ISliceable
from prompto.value.IntegerValue import IntegerValue
from prompto.error.IndexOutOfRangeError import IndexOutOfRangeError
from prompto.error.SyntaxError import SyntaxError

class BaseValueList(BaseValue, ISliceable):

    def __init__(self, type, items=None, mutable = False):
        super().__init__(type)
        if items is None:
            items = []
        self.items = items
        self.mutable = mutable

    def __str__(self):
        return str(self.items)

    def getIterator(self, context=None):
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
        if(len(other.items)==0):
            return self
        else:
            result = []
            result.extend(self.items)
            result.extend(other.items)
            return self.newInstance(result)


    def remove(self, other):
        if(len(other.items)==0):
            return self
        else:
            result = filter(lambda item: not item in other.items, self.items)
            return self.newInstance(result)


    def hasItem(self, context, lval):
        for item in self.items:
            if item == lval:
                return True
        return False


    def getItem(self, context, index):
        if isinstance(index, IntegerValue):
            try:
                idx = index.IntegerValue() - 1
                return self.items[idx]
            except IndexError:
                raise IndexOutOfRangeError()
        else:
            raise SyntaxError("No such item:" + index.toString())

    def setItem(self, context, index, value):
        if isinstance(index, IntegerValue):
            try:
                idx = index.IntegerValue() - 1
                self.items[idx] = value
            except IndexError:
                raise IndexOutOfRangeError()
        else:
            raise SyntaxError("No such item:" + str(index))


    def __eq__(self, obj):
        if not isinstance(obj, BaseValueList):
            return False
        return self.items == obj.items


    def getMemberValue(self, context, name, autoCreate=False):
        if "count" == name:
            return IntegerValue(len(self.items))
        else:
            return super(BaseValueList, self).getMemberValue(context, name)


    def toDocumentValue(self, context):
        items = [ item.toDocumentValue(context) for item in self.items ]
        from prompto.value.ListValue import ListValue
        from prompto.type.AnyType import AnyType
        return ListValue(AnyType.instance, items)


    def toJsonNode(self):
        return [ item.toJsonNode() for item in self.items ]
