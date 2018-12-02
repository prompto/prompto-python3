from prompto.error.InternalError import InternalError
from prompto.error.NullReferenceError import NullReferenceError
from prompto.error.SyntaxError import SyntaxError
from prompto.expression.IExpression import IExpression
from prompto.expression.InstanceExpression import InstanceExpression
from prompto.expression.UnresolvedIdentifier import UnresolvedIdentifier
from prompto.type.CategoryType import CategoryType
from prompto.type.DocumentType import DocumentType
from prompto.type.ListType import ListType
from prompto.type.SetType import SetType
from prompto.type.TupleType import TupleType
from prompto.value.ListValue import ListValue
from prompto.value.SetValue import SetValue
from prompto.value.TupleValue import TupleValue


class SortedExpression(IExpression):

    def __init__(self, source, desc=False, key=None):
        super(SortedExpression, self).__init__()
        self.source = source
        self.desc = desc
        self.key = key


    def __str__(self):
        return "sorted " + ("descending " if self.desc else "") + str(self.source) + ("" if self.key is None else " with " + str(self.key) + " as key")


    def check(self, context):
        itype = self.source.check(context)
        if not isinstance(itype, (ListType, TupleType, SetType)):
            raise SyntaxError("Unsupported type: " + str(itype))
        return type


    def interpret(self, context):
        itype = self.source.check(context)
        if not isinstance(itype, (ListType, TupleType, SetType)):
            raise SyntaxError("Unsupported type: " + itype)
        o = self.source.interpret(context)
        if o is None:
            raise NullReferenceError()
        if not isinstance(o, (ListValue, TupleValue, SetValue)):
            raise InternalError("Unexpected type:" + type(o).__name__)
        items = o.getIterator(context)
        itemType = itype.itemType
        if isinstance(itemType, CategoryType):
            items = itemType.sort(context, items, self.desc, self.key)
        elif itemType is DocumentType.instance:
            items = itemType.sort(context, items, self.desc, self.key)
        else:
            items = itemType.sort(context, items, self.desc)
        return ListValue(itemType, items=items)


    def setKey(self, key):
        self.key = key


    def toMDialect(self, writer):
        self.toODialect(writer)


    def toODialect(self, writer):
        writer.append("sorted ")
        if self.desc:
            writer.append("desc ")
        writer.append("(")
        self.source.toDialect(writer)
        if self.key is not None:
            writer = self.contextualizeWriter(writer)
            writer.append(", key = ")
            self.key.toDialect(writer)
        writer.append(")")


    def toEDialect(self, writer):
        writer.append("sorted ")
        if self.desc:
            writer.append("descending ")
        self.source.toDialect(writer)
        if self.key is not None:
            writer = self.contextualizeWriter(writer)
            writer.append(" with ")
            keyExp = self.key
            if isinstance(keyExp, UnresolvedIdentifier):
                try:
                    keyExp = keyExp.resolve(writer.context, False)
                except:
                    pass # TODO add warning
            if isinstance(keyExp, InstanceExpression):
                keyExp.toDialect(writer, False)
            else:
                keyExp.toDialect(writer)
            writer.append(" as key")


    def contextualizeWriter(self, writer):
        typ = self.source.check(writer.context)
        itemType = typ.itemType
        if isinstance(itemType, CategoryType):
            return writer.newInstanceWriter(itemType)
        elif isinstance(itemType, DocumentType):
            return writer.newDocumentWriter()
        else:
            return writer

