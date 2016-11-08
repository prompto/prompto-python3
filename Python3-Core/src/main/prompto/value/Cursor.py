from prompto.type.CategoryType import CategoryType
from prompto.value.BaseValue import BaseValue
from prompto.type.CursorType import CursorType
from prompto.value.IIterable import IIterable
from prompto.value.Integer import Integer
from prompto.store.InvalidValueError import InvalidValueError

class Cursor(BaseValue, IIterable):

    def __init__(self, context, itemType, stored):
        super().__init__(CursorType(itemType))
        self.context = context
        self.stored = stored
        self.mutable = getattr(itemType, "mutable", False)

    def isEmpty(self):
        return len(self.stored)==0

    def __len__(self):
        return len(self.stored)

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

    def getMember(self, context, name, autoCreate=False):
        if "count" == name:
            return Integer(len(self))
        else:
            raise InvalidValueError("No such member:" + name)


