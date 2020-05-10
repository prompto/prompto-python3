import codecs
import json
from io import BytesIO
from zipfile import ZipFile

from prompto.error.ReadWriteError import ReadWriteError
from prompto.expression.IExpression import IExpression
from prompto.type.DocumentType import DocumentType
from prompto.value.BlobValue import BlobValue
from prompto.value.DocumentValue import DocumentValue


class DocumentExpression ( IExpression ):

    def __init__(self, source):
        self.source = source

    def check(self, context):
        if self.source is not None:
            self.source.check(context)
        return DocumentType.instance

    def interpret(self, context):
        if self.source is None:
            return DocumentValue()
        else:
            value = self.source.interpret(context)
            return self.documentFromValue(context, value)

    def documentFromValue(self, context, value):
        from prompto.value.ConcreteInstance import ConcreteInstance
        if isinstance(value, BlobValue):
            return self.documentFromBlob(context, value)
        elif isinstance(value, ConcreteInstance):
            return value.toDocumentValue(context)
        else:
            raise Exception("documentFromValue not supported for " + type(value).__name__)

    def documentFromBlob(self, context, blob):
        if "application/zip"!=blob.mimeType:
            raise Exception("documentFromBlob not supported for " + blob.mimeType)
        try:
            parts = self.readParts(blob.data)
            value = self.readValue(parts)
            field = value.get("type", None)
            if field is None:
                raise Exception("Expecting a 'type' field!")
            from prompto.parser.ECleverParser import ECleverParser
            itype = ECleverParser(text=str(field)).parse_standalone_type()
            if not itype is DocumentType.instance:
                raise Exception("Expecting a Document type!")
            field = value.get("value", None)
            if field is None:
                raise Exception("Expecting a 'value' field!")
            return itype.readJSONValue(context, field, parts)
        except Exception as e:
            raise ReadWriteError(e.message)

    def readParts(self, data):
        parts = dict()
        input = BytesIO(data)
        zip = ZipFile(input, mode='r')
        try:
            for info in zip.infolist():
                parts[info.filename] = zip.read(info.filename)
            return parts
        finally:
            zip.close()

    def readValue(self, parts):
        data = parts.get("value.json", None)
        if data is None:
            raise Exception("Expecting a 'value.json' part!")
        input = BytesIO(data)
        reader = codecs.getreader("utf-8")
        return json.load(reader(input))

    def __str__(self):
        return "Document"

    def toMDialect(self, writer):
        writer.append("Document(")
        if self.source is not None:
            writer.append(" from = ")
            self.source.toDialect(writer)
        writer.append(")")

    def toODialect(self, writer):
        writer.append("Document(")
        if self.source is not None:
            writer.append(" from = ")
            self.source.toDialect(writer)
        writer.append(")")

    def toEDialect(self, writer):
        writer.append("Document")
        if self.source is not None:
            writer.append(" from ")
            self.source.toDialect(writer)
