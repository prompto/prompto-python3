from prompto.error.InternalError import InternalError
from prompto.error.NullReferenceError import NullReferenceError
from prompto.expression.IExpression import IExpression
from prompto.parser.Section import Section
from prompto.runtime.TransientVariable import TransientVariable
from prompto.type.BooleanType import BooleanType
from prompto.type.ListType import ListType
from prompto.type.TupleType import TupleType
from prompto.type.SetType import SetType
from prompto.value.ListValue import ListValue
from prompto.value.TupleValue import TupleValue
from prompto.value.SetValue import SetValue
from prompto.value.Boolean import Boolean


class FetchExpression(Section, IExpression):

    def __init__(self, itemName, source, filter_):
        super(FetchExpression, self).__init__()
        self.itemName = itemName
        self.source = source
        self.filter = filter_

    def __str__(self):
        return "fetch any " + self.itemName + " from " + str(self.source) + " where " + str(self.filter)

    def toSDialect(self, writer):
        writer.append("fetch ")
        writer.append(self.itemName)
        writer.append(" from ")
        self.source.toDialect(writer)
        writer.append(" where ")
        self.filter.toDialect(writer)

    def toEDialect(self, writer):
        writer.append("fetch any ")
        writer.append(self.itemName)
        writer.append(" from ")
        self.source.toDialect(writer)
        writer.append(" where ")
        self.filter.toDialect(writer)

    def toODialect(self, writer):
        writer.append("fetch (")
        writer.append(self.itemName)
        writer.append(")")
        writer.append(" from ")
        self.source.toDialect(writer)
        writer.append(" where ")
        self.filter.toDialect(writer)

    def check(self, context):
        listType = self.source.check(context)
        if not isinstance(listType, (ListType, TupleType, SetType)):
            raise SyntaxError("Expecting a collection type as data source !")
        local = context.newLocalContext()
        local.registerValue(TransientVariable(self.itemName, listType.getItemType()))
        filterType = self.filter.check(local)
        if filterType != BooleanType.instance:
            raise SyntaxError("Filtering expression must return a boolean !")
        return listType

    def interpret(self, context):
        listType = self.source.check(context)
        if not isinstance(listType, (ListType, TupleType, SetType)):
            raise InternalError("Illegal source type: " + listType.getName())
        itemType = listType.getItemType()
        items = self.source.interpret(context)
        if items == None:
            raise NullReferenceError()
        if not isinstance(items, (ListValue, TupleValue, SetValue)):
            raise InternalError("Illegal fetch source: " + str(items))
        result = ListValue(itemType)
        local = context.newLocalContext()
        item = TransientVariable(self.itemName, itemType)
        local.registerValue(item)
        for o in items.getItems(context):
            local.setValue(self.itemName, o)
            test = self.filter.interpret(local)
            if not isinstance(test, Boolean):
                raise InternalError("Illegal test result: " + test)
            if test.getValue():
                result.append(o)
        return result
