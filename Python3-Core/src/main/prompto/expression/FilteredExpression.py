from prompto.error.InternalError import InternalError
from prompto.error.NullReferenceError import NullReferenceError
from prompto.expression.IExpression import IExpression
from prompto.parser.Section import Section
from prompto.type.BooleanType import BooleanType
from prompto.type.IterableType import IterableType
from prompto.type.ListType import ListType
from prompto.value.IFilterable import IFilterable
from prompto.error.SyntaxError import SyntaxError


class FilteredExpression(Section, IExpression):

    def __init__(self, source, predicate):
        super(FilteredExpression, self).__init__()
        self.source = source
        self.predicate = predicate


    def __str__(self):
        return str(self.source) + "filtered with " + str(self.predicate)


    def toDialect(self, writer):
        self.predicate.filteredToDialect(writer, self.source)


    def check(self, context):
        listType = self.source.check(context)
        if not isinstance(listType, IterableType):
            raise SyntaxError("Expecting an iterable type as data source!")
        itemType = listType.itemType
        arrow = self.predicate.toArrowExpression()
        filterType = arrow.checkFilter(context, itemType)
        if filterType is not BooleanType.instance:
            raise SyntaxError("Filtering expression must return a boolean!")
        return ListType(itemType, False)


    def interpret(self, context):
        listType = self.source.check(context)
        if not isinstance(listType, IterableType):
            raise InternalError("Illegal source type: " + listType.typeName)
        itemType = listType.itemType
        items = self.source.interpret(context)
        if items is None:
            raise NullReferenceError()
        if not isinstance(items, IFilterable):
            raise InternalError("Illegal fetch source: " + str(items))
        arrow = self.predicate.toArrowExpression()
        xfilter = arrow.getFilter(context, itemType)
        return items.filter(xfilter)


