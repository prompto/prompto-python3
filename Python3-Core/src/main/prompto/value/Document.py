from prompto.type.DocumentType import DocumentType
from prompto.value.BaseValue import BaseValue
from prompto.value.Text import Text
from prompto.error.SyntaxError import SyntaxError


class Document ( BaseValue ):

    def __init__(self):
        super(Document, self).__init__(DocumentType.instance)
        self.mutable = True
        self.values = dict()

    def getMemberNames(self):
        return self.values.keys()

    def hasMember(self, name):
        result = self.values.get(name, None)
        return result is not None

    def getMember(self, context, name, autoCreate=False):
        result = self.values.get(name, None)
        if autoCreate and result is None:
            result = Document()
            self.values[name] = result
        return result



    def setMember(self, context, name, value):
        self.values[name] = value


    def getItem(self, context, index):
        if isinstance(index, Text):
            # TODO autocreate
            return self.values.get(index.value, None)
        else:
            raise SyntaxError("No such item:" + index.toString())


    def setItem(self, context, index, value):
        if isinstance(index, Text):
            self.values[index.value] = value
        else:
            raise SyntaxError("No such item:" + index.toString())


    def toJson(self, context, generator, instanceId, fieldName, binaries):
        generator.writeStartObject()
        generator.writeFieldName("type")
        generator.writeString(DocumentType.instance.name)
        generator.writeFieldName("value")
        generator.writeStartObject()
        for key, value in self.values.items():
            generator.writeFieldName(key)
            if value is None:
                generator.writeNull()
            else:
                value.toJson(context, generator, id(self), key, binaries)
        generator.writeEndObject()
        generator.writeEndObject()
