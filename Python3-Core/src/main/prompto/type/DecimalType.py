from numbers import Number

from prompto.type.BooleanType import BooleanType
from prompto.type.IType import IType
from prompto.type.NativeType import NativeType
from prompto.value.DecimalValue import DecimalValue
from prompto.store.TypeFamily import TypeFamily


class DecimalType(NativeType):
    instance = None

    def __init__(self):
        super().__init__(TypeFamily.DECIMAL)


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
        return super().checkAdd(context, other, tryReverse)


    def checkSubstract(self, context, other):
        from prompto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return self
        if isinstance(other, DecimalType):
            return self
        return super().checkSubstract(context, other)


    def checkMultiply(self, context, other, tryReverse):
        from prompto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return self
        if isinstance(other, DecimalType):
            return self
        return super().checkMultiply(context, other, tryReverse)


    def checkDivide(self, context, other):
        from prompto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return self
        if isinstance(other, DecimalType):
            return self
        return super().checkDivide(context, other)


    def checkIntDivide(self, context, other):
        from prompto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return IntegerType.instance
        return super().checkIntDivide(context, other)

    def checkModulo(self, context, other):
        from prompto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return self
        if isinstance(other, DecimalType):
            return self
        return super().checkModulo(context, other)

    def checkCompare(self, context, other):
        from prompto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return BooleanType.instance
        if isinstance(other, DecimalType):
            return BooleanType.instance
        return super().checkCompare(context, other)


    def convertPythonValueToPromptoValue(self, context, value, returnType):
        if isinstance(value, Number):
            return DecimalValue(float(value))
        else:
            return super().convertPythonValueToPromptoValue(context, value, returnType)  # TODO for now

DecimalType.instance = DecimalType()

