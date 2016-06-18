from prompto.argument.IArgument import IArgument
from prompto.type.DecimalType import DecimalType
from prompto.type.IntegerType import IntegerType
from prompto.value.Decimal import Decimal
from prompto.value.Integer import Integer



class BaseArgument ( IArgument ) :

    def __init__(self, name):
        self.name = name
        self.mutable = False
        self.defaultExpression = None

    def getName(self):
        return self.name

    def checkValue(self, context, expression):
        value = expression.interpret(context)
        if isinstance(value, Integer) and self.getType(context)==DecimalType.instance:
            return Decimal(value.DecimalValue())
        elif isinstance(value, Decimal) and self.getType(context)==IntegerType.instance:
            return Integer(value.IntegerValue())
        else:
            return value
