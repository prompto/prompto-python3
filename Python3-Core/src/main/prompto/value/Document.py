from prompto.type.DocumentType import DocumentType
from prompto.value.BaseValue import BaseValue

class Document ( BaseValue ):

    def __init__(self):
        super(Document, self).__init__(DocumentType.instance)
        self.mutable = True
        self.members = dict()

    def HasMember(self, name):
        result = self.members.get(name, None)
        return result is not None

    def GetMember(self, context, name, create = True):
        result = self.members.get(name, None)
        if create and result is None:
            result = Document()
            self.members[name] = result
        return result

    def SetMember(self, context, name, value):
        self.members[name] = value
