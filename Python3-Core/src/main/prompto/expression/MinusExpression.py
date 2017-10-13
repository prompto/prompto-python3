from prompto.expression.IUnaryExpression import IUnaryExpression
from prompto.type.DecimalType import DecimalType
from prompto.type.IntegerType import IntegerType
from prompto.type.PeriodType import PeriodType
from prompto.value.Decimal import Decimal
from prompto.value.Integer import Integer
from prompto.value.Period import Period
from prompto.error.SyntaxError import SyntaxError

class MinusExpression ( IUnaryExpression ):

    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return "-" + str(self.expression)

    def toDialect(self, writer):
        writer.append("-")
        self.expression.toDialect(writer)

    def check(self, context):
        itype = self.expression.check(context)
        if isinstance(itype, IntegerType) or isinstance(itype, DecimalType) or isinstance(itype, PeriodType):
            return itype
        else:
            raise SyntaxError("Cannot negate " + itype.getName())

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
