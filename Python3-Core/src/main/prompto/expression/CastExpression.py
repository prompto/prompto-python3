from prompto.expression.IExpression import IExpression
from prompto.error.SyntaxError import SyntaxError

class CastExpression (IExpression):

    def __init__(self, expression, type):
        self.expression = expression
        self.type = type

    def check(self, context):
        actual = self.expression.check(context)
        if not self.type.isAssignableTo(context, actual):
            raise SyntaxError("Cannot cast " + actual.toString() + " to " + self.type.toString())
        return self.type

    def interpret(self, context):
        return self.expression.interpret(context)

    def toSDialect(self, writer):
        self.toEDialect(writer)

    def toEDialect(self, writer):
        self.expression.toDialect(writer)
        writer.append(" as ")
        self.type.toDialect(writer)

    def toODialect(self, writer):
        writer.append("(")
        self.type.toDialect(writer)
        writer.append(")")
        self.expression.toDialect(writer)

