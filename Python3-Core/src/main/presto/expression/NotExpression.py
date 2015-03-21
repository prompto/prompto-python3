from presto.expression.IUnaryExpression import IUnaryExpression
from presto.type.BooleanType import BooleanType
from presto.value.Boolean import Boolean
from presto.error.SyntaxError import SyntaxError

class NotExpression ( IUnaryExpression ):

    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return "not " + str(self.expression)

    def toPDialect(self, writer):
        writer.append("not ")
        self.expression.toDialect(writer)

    def toEDialect(self, writer):
        writer.append("not ")
        self.expression.toDialect(writer)

    def toODialect(self, writer):
        writer.append("!")
        self.expression.toDialect(writer)

    def check(self, context):
        type_ = self.expression.check(context)
        if not isinstance(type_, BooleanType):
            raise SyntaxError("Cannot negate " + type_.getName())
        return BooleanType.instance

    def interpret(self, context):
        val = self.expression.interpret(context)
        if isinstance(val, Boolean):
            return val.getNot()
        else:
            raise SyntaxError("Illegal: not " + type(val).__name__)
