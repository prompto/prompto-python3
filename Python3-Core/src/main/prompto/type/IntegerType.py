from numbers import Number
from prompto.type.AnyType import *
from prompto.type.BooleanType import *
from prompto.type.CharacterType import *
from prompto.type.ListType import *
from prompto.type.NativeType import *
from prompto.type.PeriodType import *
from prompto.type.RangeType import *
from prompto.type.TextType import *
from prompto.value.Integer import *
from prompto.value.IntegerRange import *


class IntegerType(NativeType):

    instance = None

    def __init__(self):
        super(IntegerType, self).__init__("Integer")

    def isAssignableTo(self, context, other):
        from prompto.type.DecimalType import DecimalType
        return isinstance(other, IntegerType) or isinstance(other, DecimalType) or isinstance(other, AnyType)

    def checkAdd(self, context, other, tryReverse):
        from prompto.type.DecimalType import DecimalType
        if isinstance(other, IntegerType):
            return self
        if isinstance(other, DecimalType):
            return other
        return super(IntegerType, self).checkAdd(context, other, tryReverse)

    def checkSubstract(self, context, other):
        from prompto.type.DecimalType import DecimalType
        if isinstance(other, IntegerType):
            return self
        if isinstance(other, DecimalType):
            return other
        return super(IntegerType, self).checkSubstract(context, other)

    def checkMultiply(self, context, other, tryReverse):
        from prompto.type.DecimalType import DecimalType
        if isinstance(other, IntegerType):
            return self
        if isinstance(other, DecimalType):
            return other
        if isinstance(other, CharacterType):
            return TextType.instance
        if isinstance(other, TextType):
            return other
        if isinstance(other, PeriodType):
            return other
        if isinstance(other, ListType):
            return other
        return super(IntegerType, self).checkMultiply(context, other, tryReverse)

    def checkDivide(self, context, other):
        from prompto.type.DecimalType import DecimalType
        if isinstance(other, IntegerType):
            return DecimalType.instance
        if isinstance(other, DecimalType):
            return other
        return super(IntegerType, self).checkDivide(context, other)

    def checkIntDivide(self, context, other):
        if isinstance(other, IntegerType):
            return IntegerType.instance
        return super(IntegerType, self).checkIntDivide(context, other)

    def checkModulo(self, context, other):
        if isinstance(other, IntegerType):
            return IntegerType.instance
        return super(IntegerType, self).checkModulo(context, other)

    def checkCompare(self, context, other):
        from prompto.type.DecimalType import DecimalType
        if isinstance(other, IntegerType):
            return BooleanType.instance
        if isinstance(other, DecimalType):
            return BooleanType.instance
        return super(IntegerType, self).checkCompare(context, other)

    def checkRange(self, context, other):
        if isinstance(other, IntegerType):
            return RangeType(self)
        return super(IntegerType, self).checkRange(context, other)

    def newRange(self, left, right):
        if isinstance(left, Integer) and isinstance(right, Integer):
            return IntegerRange(left, right)
        return super(IntegerType, self).newRange(left, right)

    def sort(self, context, source, desc, key=None):
        return sorted(source, reverse=desc)

    def convertPythonValueToPromptoValue(self, context, value, returnType):
        if isinstance(value, Number):
            return Integer(int(value))
        else:
            return value  # TODO for now


IntegerType.instance = IntegerType()