from presto.type.DocumentType import DocumentType
from presto.value.BaseValue import BaseValue

class Document ( BaseValue ):

    def __init__(self):
        super(Document, self).__init__(DocumentType.instance)
        self.members = dict()

    def getMember(self, context, name):
        result = self.members.get(name, None)
        if result is None:
            result = Document()
            self.members[name] = result
        return result

    def setMember(self, name, value):
        self.members[name] = value
