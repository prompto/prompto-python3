from prompto.expression.IExpression import IExpression
from prompto.runtime.Variable import Variable
from prompto.error.InternalError import InternalError
from prompto.type.IteratorType import IteratorType
from prompto.value.Iterator import Iterator

class IteratorExpression(IExpression):

    def __init__(self, name, source, exp):
        self.name = name
        self.source = source
        self.expression = exp

    def check(self, context):
        srcType = self.source.check(context)
        elemType = srcType.checkIterator(context)
        child = context.newChildContext()
        context.registerValue(Variable(self.name, elemType))
        itemType = self.expression.check(child)
        return IteratorType(itemType)

    def interpret(self, context):
        iterType = self.check(context)
        itemType = iterType.getItemType()
        items = self.source.interpret(context)
        length = items.GetMember(context, "length", False)
        iterator = self.getIterator(context, items)
        return Iterator(itemType, context, length, self.name, iterator, self.expression)

    def getIterator(self, context, src):
        if getattr(src, "getIterator", None) is None:
            raise InternalError("Should never get there!")
        else:
            return src.getIterator(context)

    def toSDialect(self, writer):
        self.expression.toDialect(writer)
        writer.append(" for ")
        writer.append(self.name)
        writer.append(" in ")
        self.source.toDialect(writer)

    def toODialect(self, writer):
        self.expression.toDialect(writer)
        writer.append(" for each ( ")
        writer.append(self.name)
        writer.append(" in ")
        self.source.toDialect(writer)
        writer.append(" )")

    def toEDialect(self, writer):
        self.expression.toDialect(writer)
        writer.append(" for each ")
        writer.append(self.name)
        writer.append(" in ")
        self.source.toDialect(writer)
