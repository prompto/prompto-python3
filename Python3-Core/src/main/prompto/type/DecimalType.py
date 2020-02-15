from numbers import Number

from prompto.type.BooleanType import BooleanType
from prompto.type.IType import IType
from prompto.type.NativeType import NativeType
from prompto.value.DecimalValue import DecimalValue
from prompto.store.TypeFamily import TypeFamily


class DecimalType(NativeType):
    instance = None

    def __init__(self):
        super(DecimalType, self).__init__(TypeFamily.DECIMAL)


    def isAssignableFrom(self, context, other:IType):
        from prompto.type.IntegerType import IntegerType
        return super().isAssignableFrom(context, other) or \
            other is IntegerType.instance


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


    def convertPythonValueToPromptoValue(self, context, value, returnType):
        if isinstance(value, Number):
            return DecimalValue(float(value))
        else:
            return value  # TODO for now

DecimalType.instance = DecimalType()

