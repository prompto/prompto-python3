from io import StringIO

from prompto.error.InternalError import InternalError
from prompto.value.BaseValueList import BaseValueList
from prompto.value.IFilterable import IFilterable
from prompto.value.Integer import Integer
from prompto.error.SyntaxError import SyntaxError

class ListValue(BaseValueList, IFilterable):

    def __init__(self, itemType, items = None, item = None, mutable = False):
        from prompto.type.ListType import ListType
        super().__init__( ListType(itemType), items, mutable)
        self.storables = None
        if item is not None:
            self.items.append(item)

    def newInstance(self, items):
        return ListValue(self.itype.itemType, items=items)


    def getStorableData(self):
        if self.storables is None:
            self.storables = [item.getStorableData() for item in self.items]
        return self.storables


    def Add(self, context, value):
        from prompto.value.SetValue import SetValue
        if isinstance(value, (ListValue, SetValue)):
            return self.merge(value)
        else:
            return super().Add(context, value)


    def Multiply(self, context, value):
        if isinstance(value, Integer):
            count = value.IntegerValue()
            if count < 0:
                raise SyntaxError("Negative repeat count:" + count)
            elif count == 0:
                return ListValue(self.itype.itemType)
            elif count == 1:
                return self
            else:
                result = []
                for i in range(1,count+1):
                    result.extend(self.items)
                return ListValue(self.itype.itemType, items=result)
        else:
            raise SyntaxError("Illegal: List * " + type(value).__name__)

    def __str__(self):
        with StringIO() as sb:
            sb.write("[")
            for v in self.items:
                sb.write(str(v))
                sb.write(", ")
            len = sb.tell()
            if len > 2:
                sb.seek(len-2)
                sb.truncate(len - 2)
            sb.write("]")
            return sb.getvalue()

    def filter(self, context, itemName, filter):
        result = ListValue(self.itype.itemType)
        for o in self.getIterator(context):
            context.setValue(itemName, o)
            test = filter.interpret(context)
            from prompto.value.Boolean import Boolean
            if not isinstance(test, Boolean):
                raise InternalError("Illegal test result: " + test)
            if test.getValue():
                result.append(o)
        return result


    def collectStorables(self, list):
        for item in self.items:
            item.collectStorables(list)
