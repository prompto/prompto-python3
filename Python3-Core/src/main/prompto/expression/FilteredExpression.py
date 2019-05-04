from prompto.error.InternalError import InternalError
from prompto.error.NullReferenceError import NullReferenceError
from prompto.expression.ArrowExpression import ArrowExpression
from prompto.expression.IExpression import IExpression
from prompto.grammar.IdentifierList import IdentifierList
from prompto.parser.Section import Section
from prompto.runtime.TransientVariable import TransientVariable
from prompto.runtime.Variable import Variable
from prompto.type.BooleanType import BooleanType
from prompto.type.IterableType import IterableType
from prompto.value.IFilterable import IFilterable
from prompto.error.SyntaxError import SyntaxError


class FilteredExpression(Section, IExpression):

    def __init__(self, itemName, source, predicate):
        super(FilteredExpression, self).__init__()
        self.itemName = itemName
        self.source = source
        self.predicate = predicate


    def __str__(self):
        return "fetch any " + self.itemName + " from " + str(self.source) + " where " + str(self.predicate)


    def toDialect(self, writer):
        if self.itemName is not None:
            self.toDialectExplicit(writer)
        elif isinstance(self.predicate, ArrowExpression):
            self.predicate.filterToDialect(writer, self.source)
        else:
            raise SyntaxError("Expecting an arrow expression!")


    def toDialectExplicit(self, writer):
        writer = writer.newChildWriter()
        sourceType = self.source.check(writer.context)
        itemType = sourceType.itemType
        writer.context.registerValue(Variable(self.itemName, itemType))
        super().toDialect(writer)


    def toMDialect(self, writer):
        self.source.toDialect(writer)
        writer.append(" filtered with ")
        writer.append(self.itemName)
        writer.append(" where ")
        self.predicate.toDialect(writer)


    def toEDialect(self, writer):
        self.toMDialect(writer)


    def toODialect(self, writer):
        writer.append("filtered (")
        self.source.toDialect(writer)
        writer.append(") with (")
        writer.append(self.itemName)
        writer.append(") where (")
        self.predicate.toDialect(writer)
        writer.append(")")


    def check(self, context):
        listType = self.source.check(context)
        if not isinstance(listType, IterableType):
            raise SyntaxError("Expecting an iterable type as data source!")
        itemType = listType.itemType
        if self.itemName is not None:
            child = context.newChildContext()
            child.registerValue(TransientVariable(self.itemName, itemType))
            filterType = self.predicate.check(child)
            if filterType is not BooleanType.instance:
                raise SyntaxError("Filtering expression must return a boolean!")
        elif isinstance(self.predicate, ArrowExpression):
            pass # TODO
        else:
            raise SyntaxError("Expecting an arrow expression!")
        return listType



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
        arrow = self.toArrowExpression()
        filter = arrow.getFilter(context, itemType)
        return items.filter(filter)


    def toArrowExpression(self):
        if self.itemName is not None:
            arrow = ArrowExpression(IdentifierList(self.itemName), None, None)
            arrow.setExpression(self.predicate)
            return arrow
        elif isinstance(self.predicate, ArrowExpression):
            return self.predicate
        else:
            raise SyntaxError("Expecting an arrow expression!")


        #child = context.newChildContext()
        #item = TransientVariable(self.itemName, itemType)
        #child.registerValue(item)
