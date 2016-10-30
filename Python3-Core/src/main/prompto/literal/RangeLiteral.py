from prompto.expression.IExpression import *

class RangeLiteral(IExpression):

    def __init__(self, first, last):
        super(RangeLiteral, self).__init__()
        self.first = first
        self.last = last

    def __str__(self):
        return "[" + str(self.first) + ".." + str(self.last) + "]"

    def toDialect(self, writer):
        writer.append("[")
        self.first.toDialect(writer)
        writer.append("..")
        self.last.toDialect(writer)
        writer.append("]")

    def getFirst(self):
        return self.first

    def getLast(self):
        return self.last

    def check(self, context):
        firstType = self.first.check(context)
        lastType = self.last.check(context)
        return firstType.checkRange(context, lastType)

    def interpret(self, context):
        type = self.first.check(context)
        if "IntegerLimits" == type.typeName:
            from prompto.type.IntegerType import IntegerType
            type = IntegerType.instance
        of = self.first.interpret(context)
        ol = self.last.interpret(context)
        return type.newRange(of, ol)
