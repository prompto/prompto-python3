from prompto.expression.IExpression import IExpression
from prompto.error.SyntaxError import SyntaxError
from prompto.type.CategoryType import CategoryType
from prompto.type.DecimalType import DecimalType
from prompto.type.IntegerType import IntegerType
from prompto.value.Decimal import Decimal
from prompto.value.Integer import Integer


class CastExpression (IExpression):

    def __init__(self, expression, type):
        self.expression = expression
        self.type = type



    def check(self, context):
        actual = self.expression.check(context)
        # check upcast
        if isinstance(actual, CategoryType) and actual.isDerivedFrom(context, self.type):
            return self.type
        # check downcast
        if actual.isAssignableFrom(context, self.type):
            return self.type
        raise SyntaxError("Cannot cast " + str(actual) + " to " + str(self.type))



    def interpret(self, context):
        value = self.expression.interpret(context)
        if value is not None:
            if isinstance(value, Integer) and self.type == DecimalType.instance:
                value = Decimal(value.DecimalValue())
            elif isinstance(value, Decimal) and self.type == IntegerType.instance:
                return Integer(value.IntegerValue())
            elif self.type.isMoreSpecificThan(context, value.type):
                value.type = self.type
        return value



    def toMDialect(self, writer):
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

