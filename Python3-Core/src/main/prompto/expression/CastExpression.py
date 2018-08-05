from prompto.expression.IExpression import IExpression
from prompto.error.SyntaxError import SyntaxError
from prompto.type.AnyType import AnyType
from prompto.type.CategoryType import CategoryType
from prompto.type.DecimalType import DecimalType
from prompto.type.IntegerType import IntegerType
from prompto.value.Decimal import Decimal
from prompto.value.Integer import Integer


def anify(itype):
    if isinstance(itype, CategoryType) and itype.typeName == "Any":
        return AnyType.instance
    else:
        return itype

class CastExpression (IExpression):


    def __init__(self, expression, itype):
        self.expression = expression
        self.itype = anify(itype)


    def check(self, context):
        actual = anify(self.expression.check(context))
        # check any
        if actual == AnyType.instance:
            return self.itype
        # check upcast
        if self.itype.isAssignableFrom(context, actual):
            return self.itype
        # check downcast
        if actual.isAssignableFrom(context, self.itype):
            return self.itype
        raise SyntaxError("Cannot cast " + str(actual) + " to " + str(self.itype))



    def interpret(self, context):
        value = self.expression.interpret(context)
        if value is not None:
            if isinstance(value, Integer) and self.itype == DecimalType.instance:
                value = Decimal(value.DecimalValue())
            elif isinstance(value, Decimal) and self.itype == IntegerType.instance:
                return Integer(value.IntegerValue())
            elif self.itype.isMoreSpecificThan(context, value.itype):
                value.itype = self.itype
        return value



    def toMDialect(self, writer):
        self.toEDialect(writer)

    def toEDialect(self, writer):
        self.expression.toDialect(writer)
        writer.append(" as ")
        self.itype.toDialect(writer)

    def toODialect(self, writer):
        writer.append("(")
        self.itype.toDialect(writer)
        writer.append(")")
        self.expression.toDialect(writer)

