from prompto.literal.DictEntryList import DictEntryList
from prompto.literal.DocEntryList import DocEntryList
from prompto.literal.Literal import Literal
from prompto.type.MissingType import MissingType
from prompto.type.TextType import TextType
from prompto.value.Dictionary import Dictionary
from prompto.error.SyntaxError import SyntaxError
from prompto.utils.TypeUtils import inferElementType
from prompto.value.Document import Document


class DocumentLiteral(Literal):
    # we can only compute keys by evaluating key expressions
    # so we can't just inherit from dict
    # so we keep the full entry list.
    def __init__(self, entries=None):
        if entries is None:
            entries = DocEntryList()
        super().__init__("{}", Document())
        self.entries = entries


    def toDialect(self, writer):
        self.entries.toDialect(writer)


    def check(self, context):
        from prompto.type.DocumentType import DocumentType
        return DocumentType.instance


    def interpret(self, context):
        if len(self.entries) > 0:
            self.check(context)
            doc = Document()
            for e in self.entries:
                key = e.getKey().interpret(context)
                val = e.getValue().interpret(context)
                doc.setMember(context, key.value, val)
            return doc
        else:
            return self.value
