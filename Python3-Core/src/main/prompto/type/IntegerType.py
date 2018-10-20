from numbers import Number
from prompto.type.CharacterType import *
from prompto.type.IType import IType
from prompto.type.ListType import *
from prompto.type.PeriodType import *
from prompto.type.RangeType import *
from prompto.type.TextType import *
from prompto.value.IntegerRange import *
from prompto.store.TypeFamily import TypeFamily


class IntegerType(NativeType):

    instance = None

    def __init__(self):
        super(IntegerType, self).__init__(TypeFamily.INTEGER)

    def isAssignableFrom(self, context, other:IType):
        from prompto.type.DecimalType import DecimalType
        return super().isAssignableFrom(context, other) or \
            other is DecimalType.instance


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


    def getMemberMethods(self, context, name):
        if name == "format":
            return [FormatMethodDeclaration()]
        else:
            return super(IntegerType, self).getMemberMethods(context, name)

IntegerType.instance = IntegerType()


class FormatMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        from prompto.argument.CategoryArgument import CategoryArgument
        from prompto.literal.TextLiteral import TextLiteral
        FORMAT_ARGUMENT = CategoryArgument(TextType.instance, "format", TextLiteral('"format"'))
        super().__init__("format", FORMAT_ARGUMENT)


    def interpret(self, context):
        from prompto.value.Text import Text
        value = self.getValue(context).value
        format = context.getValue("format").value
        format = translateFormat(format)
        text = format.format(value)
        return Text(text)


    def check(self, context, isStart=False):
        from prompto.type.ListType import ListType
        return ListType(TextType.instance)


def translateFormat(f):
    leadingZeros = 0
    for c in range(0, len(f)):
        if f[c] == '0':
            leadingZeros = leadingZeros + 1
    if leadingZeros > 0:
        return "{0:0" + str(leadingZeros) + "d}"
    else:
        return "{0:d}"
