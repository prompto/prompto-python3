from prompto.error.IndexOutOfRangeError import IndexOutOfRangeError
from prompto.error.InternalError import InternalError
from prompto.error.SyntaxError import SyntaxError
from prompto.value.BaseValue import BaseValue
from prompto.value.IContainer import IContainer
from prompto.value.IFilterable import IFilterable
from prompto.value.Integer import Integer
from io import StringIO

class SetValue(BaseValue, IContainer, IFilterable):

    def __init__(self, itemType, items = None):
        from prompto.type.SetType import SetType
        super().__init__( SetType(itemType))
        self.items = items if items is not None else set()

    def isEmpty(self):
        return len(self.items)==0

    def __len__(self):
        return len(self.items)

    def getIterator(self, context=None):
        for item in self.items:
            yield item

    def hasItem(self, context, item):
        return item in self.items

    def getItem(self, context, index):
        if isinstance(index, Integer):
            idx = index.IntegerValue()
            for item in self.items:
                idx -= 1
                if idx==0:
                    return item
            raise IndexOutOfRangeError()
        else:
            raise SyntaxError("No such item:" + index.toString())


    def __eq__(self, obj):
        if not isinstance(obj, SetValue):
            return False
        return self.items==obj.items


    def __str__(self):
        with StringIO() as sb:
            sb.write("<")
            for v in self.items:
                sb.write(str(v))
                sb.write(", ")
            len = sb.tell()
            if len > 2:
                sb.truncate(len - 2)
                sb.seek(len-2)
            sb.write(">")
            return sb.getvalue()

    def Add(self, context, value):
        from prompto.value.ListValue import ListValue
        if isinstance(value, (ListValue, SetValue)):
            return self.merge(value.items)
        else:
            raise SyntaxError("Illegal: " + self.itype.typeName + " + " + type(value).__name__)


    def merge(self, items):
        if(len(items)==0):
            return self
        else:
            data = set()
            data |= self.items
            if isinstance(items, set):
                data |= items
            else:
                data |= set(items)
            return SetValue(self.itype.itemType, data)


    def Subtract(self, context, value):
        from prompto.value.ListValue import ListValue
        if isinstance(value, ListValue):
            setValue = SetValue(self.itype.itemType)
            value = setValue.Add(context, value)
        if isinstance(value, SetValue):
            return self.remove(value.items)
        else:
            return super().Subtract(context, value)


    def remove(self, items):
        if(len(items)==0):
            return self
        else:
            data = set()
            data |= self.items
            if isinstance(items, set):
                data -= items
            else:
                data -= set(items)
            return SetValue(self.itype.itemType, data)


    def filter(self, context, itemName, filter):
        result = set()
        for o in self.getIterator(context):
            context.setValue(itemName, o)
            test = filter.interpret(context)
            from prompto.value.Boolean import Boolean
            if not isinstance(test, Boolean):
                raise InternalError("Illegal test result: " + test)
            if test.getValue():
                result.add(o)
        return SetValue(self.itype.itemType, result)

    def getMemberValue(self, context, name, autoCreate=False):
        if "count" == name:
            return Integer(len(self.items))
        else:
            return super(SetValue, self).getMemberValue(context, name)

