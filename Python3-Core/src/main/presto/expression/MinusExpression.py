from presto.expression.IUnaryExpression import IUnaryExpression
from presto.type.DecimalType import DecimalType
from presto.type.IntegerType import IntegerType
from presto.type.PeriodType import PeriodType
from presto.value.Decimal import Decimal
from presto.value.Integer import Integer
from presto.value.Period import Period
from presto.error.SyntaxError import SyntaxError

class MinusExpression ( IUnaryExpression ):

    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return "-" + str(self.expression)

    def toDialect(self, writer):
        writer.append("-")
        self.expression.toDialect(writer)

    def check(self, context):
        type_ = self.expression.check(context)
        if isinstance(type_, IntegerType) or isinstance(type_, DecimalType) or isinstance(type_, PeriodType):
            return type_
        else:
            raise SyntaxError("Cannot negate " + type_.getName())

    def interpret(self, context):
        val = self.expression.interpret(context)
        if isinstance(val, Integer):
            return Integer(-val.IntegerValue())
        elif isinstance(val, Decimal):
            return Decimal(-val.DecimalValue())
        elif isinstance(val, Period):
            return val.inverse()
        else:
            raise SyntaxError("Illegal: - " + type(val).__name__)

    def getExpression(self):
        return self.expression
