from prompto.value.BaseValue import BaseValue
from prompto.value.INumber import INumber
from prompto.value.IMultiplyable import IMultiplyable
from prompto.value.Decimal import Decimal
from prompto.error.DivideByZeroError import DivideByZeroError
from prompto.error.SyntaxError import SyntaxError

class Integer(BaseValue, INumber, IMultiplyable):

    @staticmethod
    def Parse(text):
        return Integer(int(text))

    def __init__(self, value):
        from prompto.type.IntegerType import IntegerType
        super().__init__(IntegerType.instance)
        self.value = value

    def convertToPython(self):
        return self.value

    def IntegerValue(self):
        return self.value

    def DecimalValue(self):
        return float(self.value)

    def Add(self, context, value):
        if isinstance(value, Integer):
            return Integer(self.IntegerValue() + value.IntegerValue())
        elif isinstance(value, Decimal):
            return Decimal(value.DecimalValue() + self.value)
        else:
            raise SyntaxError("Illegal: Integer + " + type(value).__name__)

    def Subtract(self, context, value):
        if isinstance(value, Integer):
            return Integer(self.IntegerValue() - value.IntegerValue())
        elif isinstance(value, Decimal):
            return Decimal(self.DecimalValue() - value.DecimalValue())
        else:
            raise SyntaxError("Illegal: Integer - " + type(value).__name__)

    def Multiply(self, context, value):
        if isinstance(value, Integer):
            return Integer(self.IntegerValue() * value.IntegerValue())
        elif isinstance(value, Decimal):
            return Decimal(value.DecimalValue() * self.IntegerValue())
        elif isinstance(value, IMultiplyable):
            return value.Multiply(context, self)
        else:
            raise SyntaxError("Illegal: Integer * " + type(value).__name__)

    def Divide(self, context, value):
        if isinstance(value, INumber):
            if value.DecimalValue() == 0.0:
                raise DivideByZeroError()
            else:
                return Decimal(self.DecimalValue() / value.DecimalValue())
        else:
            raise SyntaxError("Illegal: Integer / " + type(value).__name__)

    def IntDivide(self, context, value):
        if isinstance(value, Integer):
            if value.IntegerValue() == 0:
                raise DivideByZeroError()
            else:
                return Integer(int(self.IntegerValue() / value.IntegerValue()))
        else:
            raise SyntaxError("Illegal: Integer \\ " + type(value).__name__)

    def Modulo(self, context, value):
        if isinstance(value, Integer):
            mod = value.IntegerValue()
            if mod == 0:
                raise DivideByZeroError()
            return Integer(self.IntegerValue() % mod)
        else:
            raise SyntaxError("Illegal: Integer % " + type(value).__name__)

    def compareTo(self, context, value):
        if isinstance(value, Integer):
            if self.IntegerValue() < value.IntegerValue():
                return -1
            elif self.IntegerValue() == value.IntegerValue():
                return 0
            else:
                return 1
        elif isinstance(value, Decimal):
            if self.DecimalValue() < value.DecimalValue():
                return -1
            elif self.DecimalValue() == value.DecimalValue():
                return 0
            else:
                return 1
        else:
            raise SyntaxError("Illegal comparison: Integer and " + type(value).__name__)

    def ConvertTo(self, type_):
        return self.value

    def __str__(self):
        return str(self.value)

    def __lt__(self, obj):
        return self.value < obj.value

    def __eq__(self, obj):
        return self.value==obj.value

    def __hash__(self):
        return hash(self.value)

    def toJson(self, context, generator, instanceId, fieldName, binaries):
        generator.writeLong(self.value)