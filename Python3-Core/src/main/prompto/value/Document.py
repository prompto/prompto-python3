from prompto.type.DocumentType import DocumentType
from prompto.value.BaseValue import BaseValue

class Document ( BaseValue ):

    def __init__(self):
        super(Document, self).__init__(DocumentType.instance)
        self.mutable = True
        self.values = dict()

    def HasMember(self, name):
        result = self.values.get(name, None)
        return result is not None

    def GetMember(self, context, name, autoCreate=False):
        result = self.values.get(name, None)
        if autoCreate and result is None:
            result = Document()
            self.values[name] = result
        return result

    def SetMember(self, context, name, value):
        self.values[name] = value

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
