from prompto.literal.DictEntryList import DictEntryList
from prompto.literal.Literal import Literal
from prompto.type.MissingType import MissingType
from prompto.type.TextType import TextType
from prompto.value.Dictionary import Dictionary


class DictLiteral(Literal):
    # we can only compute keys by evaluating key expressions
    # so we can't just inherit from dict
    # so we keep the full entry list.
    def __init__(self, entries=None):
        if entries is None:
            entries = DictEntryList()
        super().__init__(str(entries), Dictionary(MissingType.instance))
        self.entries = entries
        self.itemType = None

    def toDialect(self, writer):
        self.entries.toDialect(writer)

    def check(self, context):
        from prompto.type.DictType import DictType
        if self.itemType is None:
            self.itemType = self.inferElementType(context)
        return DictType(self.itemType)

    def inferElementType(self, context):
        if len(self.entries) == 0:
            return MissingType.instance
        lastType = None
        for e in self.entries:
            keyType = e.getKey().check(context)
            if keyType != TextType.instance:
                raise SyntaxError("Illegal key type: " + keyType.toString())
            elemType = e.getValue().check(context)
            if lastType is None:
                lastType = elemType
            elif lastType != elemType:
                if elemType.isAssignableTo(context, lastType):
                    pass  # lastType is less specific
                elif lastType.isAssignableTo(context, elemType):
                    lastType = elemType  # elemType is less specific
                else:
                    raise SyntaxError(
                        "Incompatible value types: " + elemType.toString() + " and " + lastType.toString())
        return lastType

    def interpret(self, context):
        if self.value.size() != 0 or len(self.entries) == 0:
            return self.value
        self.check(context)
        value = dict()
        for e in self.entries:
            key = e.getKey().interpret(context)
            val = e.getValue().interpret(context)
            value[key.value] = val
        self.value = Dictionary(self.itemType, value=value)
        return self.value
