from io import StringIO

from prompto.error.InternalError import InternalError
from prompto.type.CategoryType import CategoryType
from prompto.value.BaseValue import BaseValue
from prompto.type.CursorType import CursorType
from prompto.value.Boolean import Boolean
from prompto.value.IFilterable import IFilterable
from prompto.value.IIterable import IIterable
from prompto.value.Integer import Integer
from prompto.store.InvalidValueError import InvalidValueError
from prompto.value.ListValue import ListValue


class Cursor(BaseValue, IIterable, IFilterable):

    def __init__(self, context, itemType, stored):
        super().__init__(CursorType(itemType))
        self.context = context
        self.stored = stored
        self.mutable = getattr(itemType, "mutable", False)


    def isEmpty(self):
        return len(self.stored)==0


    def __len__(self):
        return len(self.stored)


    def totalLength(self):
        return self.stored.totalLength()


    def __str__(self):
        with StringIO() as sb:
            sb.write("[")
            for v in self.getIterator(self.context):
                sb.write(str(v))
                sb.write(", ")
            len = sb.tell()
            if len > 2:
                sb.seek(len-2)
                sb.truncate(len - 2)
            sb.write("]")
            return sb.getvalue()


    def getIterator(self, context):
        for stored in self.stored:
            typ = self.readItemType(stored)
            val = typ.newInstanceFromStored(context, stored)
            yield val


    def readItemType(self, stored):
        # val = getattr(stored, "category")
        # category = val[-1]
        category = stored.categories[-1]
        typ = CategoryType(category)
        typ.mutable = self.mutable
        return typ


    def getMemberValue(self, context, name, autoCreate=False):
        if "count" == name:
            return Integer(len(self))
        elif "totalCount" == name:
            return Integer(self.totalLength())
        else:
            raise InvalidValueError("No such member:" + name)


    def filter(self, predicate):
        return FilteredCursor(self, predicate)


    def toListValue(self, context):
        items = [ item for item in self.getIterator(context)]
        return ListValue(self.itype.itemType, items=items)


class FilteredCursor(Cursor):

    def __init__(self, cursor, predicate):
        super().__init__(cursor.context, cursor.itype.itemType, cursor.stored)
        self.predicate = predicate


    def getIterator(self, context):
        for stored in self.stored:
            typ = self.readItemType(stored)
            val = typ.newInstanceFromStored(self.context, stored)
            if self.predicate(val):
                yield val

