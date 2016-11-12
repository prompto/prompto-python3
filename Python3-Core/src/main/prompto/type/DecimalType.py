from prompto.type.IType import IType
from prompto.type.IntegerType import *
from prompto.type.NativeType import *
from prompto.value.Decimal import *
from prompto.store.TypeFamily import TypeFamily


class DecimalType(NativeType):
    instance = None

    def __init__(self):
        super(DecimalType, self).__init__(TypeFamily.DECIMAL)


    def isAssignableFrom(self, context, other:IType):
        from prompto.type.IntegerType import IntegerType
        return super().isAssignableFrom(context, other) or \
            other == IntegerType.instance


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


    def sort(self, context, source, desc):
        return sorted(source, reverse=desc)

    def convertPythonValueToPromptoValue(self, context, value, returnType):
        if isinstance(value, Number):
            return Decimal(float(value))
        else:
            return value  # TODO for now

DecimalType.instance = DecimalType()

