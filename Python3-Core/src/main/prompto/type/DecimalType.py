from numbers import Number
from prompto.type.AnyType import *
from prompto.type.BooleanType import *
from prompto.type.IntegerType import *
from prompto.type.NativeType import *
from prompto.value.Decimal import *


class DecimalType(NativeType):
    instance = None

    def __init__(self):
        super(DecimalType, self).__init__("Decimal")

    def isAssignableTo(self, context, other):
        from prompto.type.AnyType import AnyType
        from prompto.type.IntegerType import IntegerType
        return isinstance(other, IntegerType) or isinstance(other, DecimalType) or isinstance(other, AnyType)

    def checkAdd(self, context, other, tryReverse):
        from prompto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return self
        if isinstance(other, DecimalType):
            return self
        return super(DecimalType, self).checkAdd(context, other, tryReverse)

    def checkSubstract(self, context, other):
        from prompto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return self
        if isinstance(other, DecimalType):
            return self
        return super(DecimalType, self).checkSubstract(context, other)


    def checkMultiply(self, context, other, tryReverse):
        from prompto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return self
        if isinstance(other, DecimalType):
            return self
        return super(DecimalType, self).checkMultiply(context, other, tryReverse)


    def checkDivide(self, context, other):
        from prompto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return self
        if isinstance(other, DecimalType):
            return self
        return super(DecimalType, self).checkDivide(context, other)


    def checkIntDivide(self, context, other):
        from prompto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return IntegerType.instance
        return super(DecimalType, self).checkIntDivide(context, other)

    def checkModulo(self, context, other):
        from prompto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return self
        if isinstance(other, DecimalType):
            return self
        return super(DecimalType, self).checkModulo(context, other)

    def checkCompare(self, context, other):
        from prompto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return BooleanType.instance
        if isinstance(other, DecimalType):
            return BooleanType.instance
        return super(DecimalType, self).checkCompare(context, other)


    def sort(self, context, source):
        return sorted(source)

    def convertPythonValueToPromptoValue(self, context, value, returnType):
        if isinstance(value, Number):
            return Decimal(float(value))
        else:
            return value  # TODO for now

DecimalType.instance = DecimalType()

