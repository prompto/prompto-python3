from io import BytesIO

from prompto.type.DocumentType import DocumentType
from prompto.utils.JSONGenerator import JSONGenerator
from prompto.value.BaseValue import BaseValue
from prompto.value.NullValue import NullValue
from prompto.value.Text import Text
from prompto.error.SyntaxError import SyntaxError


class Document ( BaseValue ):

    def __init__(self):
        super(Document, self).__init__(DocumentType.instance)
        self.mutable = True
        self.values = dict()


    def getStorableData(self):
        return self.values


    def getMemberNames(self):
        return self.values.keys()

    def hasMember(self, name):
        result = self.values.get(name, None)
        return result is not None

    def getMemberValue(self, context, name, autoCreate = False):
        result = self.values.get(name, None)
        if result is not None:
            return result
        elif "text" == name:
            return Text(str(self))
        elif autoCreate:
            result = Document()
            self.values[name] = result
            return result
        else:
            return NullValue.instance

    def setMember(self, context, name, value):
        self.values[name] = value


    def getItem(self, context, index):
        if isinstance(index, Text):
            # TODO autocreate
            return self.values.get(index.value, NullValue.instance)
        else:
            raise SyntaxError("No such item:" + index.toString())


    def setItem(self, context, index, value):
        if isinstance(index, Text):
            self.values[index.value] = value
        else:
            raise SyntaxError("No such item:" + index.toString())

    def __str__(self):
        binaries = dict()
        # create textual data
        output = BytesIO()
        generator = JSONGenerator(output)
        generator.writeStartObject()
        for key, value in self.values.items():
            generator.writeFieldName(key)
            if value is None:
                generator.writeNull()
            else:
                value.toJson(None, generator, id(self), key, False, binaries)
        generator.writeEndObject()
        # done
        output.flush()
        return output.getvalue().decode()


    def toJson(self, context, generator, instanceId, fieldName, withType, binaries):
        if withType:
            generator.writeStartObject()
            generator.writeFieldName("type")
            generator.writeString(DocumentType.instance.typeName)
            generator.writeFieldName("value")
        generator.writeStartObject()
        for key, value in self.values.items():
            generator.writeFieldName(key)
            if value is None:
                generator.writeNull()
            else:
                value.toJson(context, generator, id(self), key, withType, binaries)
        generator.writeEndObject()
        if withType:
            generator.writeEndObject()
