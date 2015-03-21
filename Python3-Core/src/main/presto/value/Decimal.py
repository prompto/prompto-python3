from presto.value.BaseValue import BaseValue
from presto.value.INumber import INumber
from presto.value.IMultiplyable import IMultiplyable
from presto.error.DivideByZeroError import DivideByZeroError
from presto.error.SyntaxError import SyntaxError


class Decimal(BaseValue, INumber, IMultiplyable):

    @staticmethod
    def Parse(text):
        return Decimal(float(text))

    def __init__(self, value):
        from presto.type.DecimalType import DecimalType
        super().__init__(DecimalType.instance)
        self.value = value

    def convertToPython(self):
        return self.value

    def IntegerValue(self):
        return int(self.value)

    def DecimalValue(self):
        return self.value

    def Add(self, context, value):
        from presto.value.Integer import Integer
        if isinstance(value, Integer):
            return Decimal(self.value + value.IntegerValue())
        elif isinstance(value, Decimal):
            return Decimal(self.value + value.DecimalValue())
        else:
            raise SyntaxError("Illegal: Decimal + " + type(value).__name__)

    def Subtract(self, context, value):
        from presto.value.Integer import Integer
        if isinstance(value, Integer):
            return Decimal(self.value - value.IntegerValue())
        elif isinstance(value, Decimal):
            return Decimal(self.value - value.DecimalValue())
        else:
            raise SyntaxError("Illegal: Decimal - " + type(value).__name__)


    def Multiply(self, context, value):
        from presto.value.Integer import Integer
        if isinstance(value, Integer):
            return Decimal(self.DecimalValue() * value.IntegerValue())
        elif isinstance(value, Decimal):
            return Decimal(self.DecimalValue() * value.DecimalValue())
        else:
            raise SyntaxError("Illegal: Decimal * " + type(value).__name__)


    def Divide(self, context, value):
        if isinstance(value, INumber):
            if value.DecimalValue() == 0.0:
                raise DivideByZeroError()
            else:
                return Decimal(self.DecimalValue() / value.DecimalValue())
        else:
            raise SyntaxError("Illegal: Decimal / " + type(value).__name__)

    def IntDivide(self, context, value):
        from presto.value.Integer import Integer
        if isinstance(value, Integer):
            if value.IntegerValue() == 0.:
                raise DivideByZeroError()
            else:
                return Integer(self.IntegerValue() / value.IntegerValue())
        else:
            raise SyntaxError("Illegal: Decimal / " + type(value).__name__)

    def Modulo(self, context, value):
        if isinstance(value, INumber):
            if value.DecimalValue() == 0.0:
                raise DivideByZeroError()
            else:
                return Decimal(self.DecimalValue() % value.DecimalValue())
        else:
            raise SyntaxError("Illegal: Decimal % " + type(value).__name__)

    def compareTo(self, context, value):
        if isinstance(value, INumber):
            if self.value < value.DecimalValue():
                return -1
            elif self.value == value.DecimalValue():
                return 0
            else:
                return 1
        else:
            raise SyntaxError("Illegal comparison: Decimal and " + type(value).__name__)


    def ConvertTo(self, type_):
        return self.value

    def __lt__(self, obj):
        return self.value < obj.value

    def __str__(self):
        return str(self.value)  #.ToString("0.0######")


    def __eq__(self, obj):
        if isinstance(obj, INumber):
            return self.value == obj.value
        else:
            return False

    def __hash__(self):
        return hash(self.value)
