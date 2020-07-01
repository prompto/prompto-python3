from prompto.literal.DocEntryList import DocEntryList
from prompto.literal.Literal import Literal
from prompto.value.DocumentValue import DocumentValue


class DocumentLiteral(Literal):
    # we can only compute keys by evaluating key expressions
    # so we can't just inherit from dict
    # so we keep the full entry list.
    def __init__(self, entries=None):
        if entries is None:
            entries = DocEntryList()
        super().__init__("{}", DocumentValue())
        self.entries = entries


    def toDialect(self, writer):
        self.entries.toDialect(writer)


    def check(self, context):
        from prompto.type.DocumentType import DocumentType
        return DocumentType.instance


    def interpret(self, context):
        if len(self.entries) > 0:
            self.check(context)
            doc = DocumentValue()
            for e in self.entries:
                key = e.getKey().interpret(context)
                val = e.getValue().interpret(context)
                doc.setMember(context, key.value, val)
            return doc
        else:
            return self.value
