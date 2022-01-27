from prompto.value.BaseValue import BaseValue
from prompto.value.INumber import INumber
from prompto.value.IMultiplyable import IMultiplyable
from prompto.value.DecimalValue import DecimalValue
from prompto.error.DivideByZeroError import DivideByZeroError
from prompto.error.SyntaxError import SyntaxError

class IntegerValue(BaseValue, INumber, IMultiplyable):

    @staticmethod
    def Parse(text):
        return IntegerValue(int(text))

    def __init__(self, value):
        from prompto.type.IntegerType import IntegerType
        super().__init__(IntegerType.instance)
        self.value = value


    def getStorableData(self):
        return self.value


    def convertToPython(self):
        return self.value


    def IntegerValue(self):
        return self.value


    def DecimalValue(self):
        return float(self.value)


    def Add(self, context, value):
        if isinstance(value, IntegerValue):
            return IntegerValue(self.IntegerValue() + value.IntegerValue())
        elif isinstance(value, DecimalValue):
            return DecimalValue(value.DecimalValue() + self.value)
        else:
            raise SyntaxError("Illegal: Integer + " + type(value).__name__)


    def Subtract(self, context, value):
        if isinstance(value, IntegerValue):
            return IntegerValue(self.IntegerValue() - value.IntegerValue())
        elif isinstance(value, DecimalValue):
            return DecimalValue(self.DecimalValue() - value.DecimalValue())
        else:
            raise SyntaxError("Illegal: Integer - " + type(value).__name__)


    def Multiply(self, context, value):
        if isinstance(value, IntegerValue):
            return IntegerValue(self.IntegerValue() * value.IntegerValue())
        elif isinstance(value, DecimalValue):
            return DecimalValue(value.DecimalValue() * self.IntegerValue())
        elif isinstance(value, IMultiplyable):
            return value.Multiply(context, self)
        else:
            raise SyntaxError("Illegal: Integer * " + type(value).__name__)


    def Divide(self, context, value):
        if isinstance(value, INumber):
            if value.DecimalValue() == 0.0:
                raise DivideByZeroError()
            else:
                return DecimalValue(self.DecimalValue() / value.DecimalValue())
        else:
            raise SyntaxError("Illegal: Integer / " + type(value).__name__)


    def IntDivide(self, context, value):
        if isinstance(value, IntegerValue):
            if value.IntegerValue() == 0:
                raise DivideByZeroError()
            else:
                return IntegerValue(int(self.IntegerValue() // value.IntegerValue()))
        else:
            raise SyntaxError("Illegal: Integer \\ " + type(value).__name__)


    def Modulo(self, context, value):
        if isinstance(value, IntegerValue):
            mod = value.IntegerValue()
            if mod == 0:
                raise DivideByZeroError()
            return IntegerValue(self.IntegerValue() % mod)
        else:
            raise SyntaxError("Illegal: Integer % " + type(value).__name__)


    def compareTo(self, context, value):
        if isinstance(value, IntegerValue):
            if self.IntegerValue() < value.IntegerValue():
                return -1
            elif self.IntegerValue() == value.IntegerValue():
                return 0
            else:
                return 1
        elif isinstance(value, DecimalValue):
            if self.DecimalValue() < value.DecimalValue():
                return -1
            elif self.DecimalValue() == value.DecimalValue():
                return 0
            else:
                return 1
        else:
            raise SyntaxError("Illegal comparison: Integer and " + type(value).__name__)

    def ConvertTo(self, itype):
        return self.value


    def __str__(self):
        return str(self.value)


    def __lt__(self, obj):
        return self.value < obj.value


    def __eq__(self, obj):
        return isinstance(obj, (IntegerValue, DecimalValue) ) and self.value == obj.value


    def __hash__(self):
        return hash(self.value)


    def toJson(self, context, generator, instanceId, fieldName, withType, binaries):
        generator.writeLong(self.value)


    def toJsonNode(self):
        return self.value
