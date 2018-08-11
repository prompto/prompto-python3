from prompto.literal.DictEntryList import DictEntryList
from prompto.literal.Literal import Literal
from prompto.type.MissingType import MissingType
from prompto.type.TextType import TextType
from prompto.value.Dictionary import Dictionary
from prompto.error.SyntaxError import SyntaxError
from prompto.utils.TypeUtils import inferElementType

class DictLiteral(Literal):
    # we can only compute keys by evaluating key expressions
    # so we can't just inherit from dict
    # so we keep the full entry list.
    def __init__(self, mutable, entries=None):
        if entries is None:
            entries = DictEntryList()
        super().__init__("<:>", Dictionary(MissingType.instance, mutable))
        self.mutable = mutable
        self.entries = entries
        self.itemType = None


    def toDialect(self, writer):
        if self.mutable:
            writer.append("mutable ")
        self.entries.toDialect(writer)


    def check(self, context):
        from prompto.type.DictType import DictType
        if self.itemType is None:
            self.itemType = self.inferElementType(context)
        return DictType(self.itemType)



    def inferElementType(self, context):
        if len(self.entries) == 0:
            return MissingType.instance
        expressions = [e.getValue() for e in self.entries]
        return inferElementType(context, expressions)



    def interpret(self, context):
        if len(self.entries) > 0:
            self.check(context)
            value = dict()
            for e in self.entries:
                key = e.getKey().asText()
                val = e.getValue().interpret(context)
                value[key.value] = val
            return Dictionary(self.itemType, self.mutable, value=value)
        else:
            return self.value
