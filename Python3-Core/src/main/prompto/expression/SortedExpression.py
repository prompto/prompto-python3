from prompto.error.InternalError import InternalError
from prompto.error.NullReferenceError import NullReferenceError
from prompto.error.SyntaxError import SyntaxError
from prompto.expression.IExpression import IExpression
from prompto.expression.InstanceExpression import InstanceExpression
from prompto.expression.UnresolvedIdentifier import UnresolvedIdentifier
from prompto.type.CategoryType import CategoryType
from prompto.type.ListType import ListType
from prompto.type.SetType import SetType
from prompto.type.TupleType import TupleType
from prompto.value.ListValue import ListValue
from prompto.value.SetValue import SetValue
from prompto.value.TupleValue import TupleValue


class SortedExpression(IExpression):

    def __init__(self, source, key=None):
        super(SortedExpression, self).__init__()
        self.source = source
        self.key = key

    def __str__(self):
        return "sorted " + str(self.source) + ("" if self.key is None else " with " + str(self.key) + " as key")

    def check(self, context):
        type_ = self.source.check(context)
        if not isinstance(type_, (ListType, TupleType, SetType)):
            raise SyntaxError("Unsupported type: " + str(type_))
        return type

    def interpret(self, context):
        type_ = self.source.check(context)
        if not isinstance(type_, (ListType, TupleType, SetType)):
            raise SyntaxError("Unsupported type: " + type_)
        o = self.source.interpret(context)
        if o is None:
            raise NullReferenceError()
        if not isinstance(o, (ListValue, TupleValue, SetValue)):
            raise InternalError("Unexpected type:" + type(o).__name__)
        items = o.getIterator(context)
        itemType = type_.getItemType()
        if isinstance(itemType, CategoryType):
            items = itemType.sort(context, items, self.key)
        else:
            items = itemType.sort(context, items)
        return ListValue(itemType, items=items)

    def setKey(self, key):
        self.key = key

    def toSDialect(self, writer):
        self.toODialect(writer)

    def toODialect(self, writer):
        writer.append("sorted (")
        self.source.toDialect(writer)
        if self.key is not None:
            writer.append(", key = ")
            self.key.toDialect(writer)
        writer.append(")")

    def toEDialect(self, writer):
        writer.append("sorted ")
        self.source.toDialect(writer)
        if self.key is not None:
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

