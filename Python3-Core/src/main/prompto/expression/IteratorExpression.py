from prompto.expression.IExpression import IExpression
from prompto.runtime.Variable import Variable
from prompto.error.InternalError import InternalError
from prompto.type.IteratorType import IteratorType
from prompto.value.IterableValue import IterableValue

class IteratorExpression(IExpression):

    def __init__(self, name, source, exp):
        self.name = name
        self.source = source
        self.expression = exp

    def check(self, context):
        elemType = self.source.check(context).checkIterator(context)
        child = context.newChildContext()
        context.registerValue(Variable(self.name, elemType))
        itemType = self.expression.check(child)
        return IteratorType(itemType)

    def interpret(self, context):
        elemType = self.source.check(context).checkIterator(context)
        items = self.source.interpret(context)
        length = items.getMemberValue(context, "count", False)
        iterator = self.getIterator(context, items)
        return IterableValue(context, self.name, elemType, iterator, length, self.expression)

    def getIterator(self, context, src):
        if getattr(src, "getIterator", None) is None:
            raise InternalError("Should never get there!")
        else:
            return src.getIterator(context)

    def toMDialect(self, writer):
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
