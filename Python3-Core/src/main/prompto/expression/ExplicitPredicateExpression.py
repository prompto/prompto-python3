from prompto.expression.ArrowExpression import ArrowExpression
from prompto.expression.IExpression import IExpression
from prompto.expression.PredicateExpression import PredicateExpression
from prompto.grammar.IdentifierList import IdentifierList
from prompto.parser.Dialect import Dialect
from prompto.runtime.Variable import Variable


class ExplicitPredicateExpression(PredicateExpression, IExpression):

    def __init__(self, itemName: str, predicate: IExpression):
        self.itemName = itemName
        self.predicate = predicate


    def toArrowExpression(self) -> ArrowExpression:
        arrow = ArrowExpression(IdentifierList(self.itemName), None, None)
        arrow.setExpression(self.predicate)
        return arrow


    def __str__(self):
        return "" + self.itemName + " where " + str(self.predicate)


    def filteredToDialect(self, writer, source):
        writer = writer.newChildWriter()
        sourceType = source.check(writer.context)
        itemType = sourceType.itemType
        writer.context.registerValue(Variable(self.itemName, itemType))
        if writer.dialect is Dialect.O:
            writer.append("filtered (")
            source.ToDialect(writer)
            writer.append(") with (") \
                .append(self.itemName) \
                .append(") where (")
            self.predicate.toDialect(writer)
            writer.append(")")
        else:
            source.toDialect(writer)
            writer.append(" filtered with ") \
                .append(self.itemName) \
                .append(" where ")
            self.predicate.toDialect(writer)


    def containsToDialect(self, writer):
        if writer.dialect is Dialect.O:
            writer.append(" (") \
                .append(self.itemName) \
                .append(") where (")
            self.predicate.toDialect(writer)
            writer.append(")")
        else:
            writer.append(" ") \
                .append(self.itemName) \
                .append(" where ")
            self.predicate.toDialect(writer)


    def checkFilter(self, context, itemType):
        child = context.newChildContext()
        child.registerValue(Variable(self.itemName, itemType))
        return self.predicate.check(child)


    def interpret(self, context):
        return self.toArrowExpression().interpret(context)



