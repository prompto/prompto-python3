

from prompto.expression.IExpression import IExpression
from prompto.type.DocumentType import DocumentType
from prompto.value.Document import Document


class DocumentExpression ( IExpression ):

    def check(self, context):
        return DocumentType.instance

    def interpret(self, context):
        return Document()

    def __str__(self):
        return "Document"

    def toSDialect(self, writer):
        writer.append("Document()")

    def toODialect(self, writer):
        writer.append("Document()")

    def toEDialect(self, writer):
        writer.append("Document")
