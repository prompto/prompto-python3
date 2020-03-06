from prompto.param.IParameter import IParameter
from prompto.type.DecimalType import DecimalType
from prompto.type.IntegerType import IntegerType
from prompto.value.DecimalValue import DecimalValue
from prompto.value.IntegerValue import IntegerValue



class BaseParameter (IParameter) :

    def __init__(self, name):
        self.name = name
        self.mutable = False
        self.defaultExpression = None


    def getName(self):
        return self.name


    def setMutable(self, mutable):
        self.mutable = mutable


    def checkValue(self, context, expression):
        value = expression.interpret(context)
        if isinstance(value, IntegerValue) and self.getType(context)==DecimalType.instance:
            return DecimalValue(value.DecimalValue())
        elif isinstance(value, DecimalValue) and self.getType(context)==IntegerType.instance:
            return IntegerValue(value.IntegerValue())
        else:
            return value
