from prompto.value.BaseValue import BaseValue
from prompto.type.CursorType import CursorType
from prompto.value.ICursor import ICursor
from prompto.value.Integer import Integer

class Cursor(BaseValue, ICursor):

    def __init__(self, context, itemType, documents):
        super().__init__(CursorType(itemType))
        self.context = context
        self.documents = documents

    def isEmpty(self):
        return len(self.documents)==0

    def __len__(self):
        return len(self.documents)

    def getItems(self, context):
        for doc in self.documents:
            val = self.type.itemType.newInstanceFromDocument(context, doc)
            yield val

    def GetMember(self, context, name):
        if "length" == name:
            return Integer(len(self))
        else:
            raise InvalidDataError("No such member:" + name)


