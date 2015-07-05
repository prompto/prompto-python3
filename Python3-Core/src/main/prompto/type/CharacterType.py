from prompto.error.InvalidDataError import InvalidDataError
from prompto.type.AnyType import *
from prompto.type.BooleanType import *
from prompto.type.NativeType import *
from prompto.type.RangeType import *
from prompto.type.TextType import TextType
from prompto.value.Character import *
from prompto.value.CharacterRange import *


class CharacterType(NativeType):
    instance = None

    def __init__(self):
        super(CharacterType, self).__init__("Character")

    def isAssignableTo(self, context, other):
        return isinstance(other, CharacterType) or isinstance(other, TextType) or isinstance(other, AnyType)

    def checkAdd(self, context, other, tryReverse):
        return TextType.instance

    def checkMultiply(self, context, other, tryReverse):
        from prompto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return TextType.instance
        else:
            return super(CharacterType, self).checkMultiply(context, other, tryReverse)

    def checkCompare(self, context, other):
        if isinstance(other, CharacterType) or isinstance(other, TextType):
            return BooleanType.instance
        return super(CharacterType, self).checkCompare(context, other)

    def checkRange(self, context, other):
        if isinstance(other, CharacterType):
            return RangeType(self)
        return super(CharacterType, self).checkRange(context, other)

    def newRange(self, left, right):
        if isinstance(left, Character) and isinstance(right, Character):
            return CharacterRange(left, right)
        return super(CharacterType, self).newRange(left, right)

    def sort(self, context, list_):

        def compare(o1, o2):
            return o1.compareTo(o2)

        return sorted(list_, cmp=compare)

    def toString(self, value):
        return "'" + str(value) + "'";

    def convertPythonValueToPrestoValue(self, context, value, returnType):
        if isinstance(value, basestring):
            return Character(value)
        else:
            return value  # TODO for now

    def nativeCast(self, context, value):
        if isinstance(value.type, TextType) and len(value.value)>=1:
            return Character(value.value[0:1])
        else:
            raise InvalidDataError("Cannot convert " + str(value) + " to Character")

CharacterType.instance = CharacterType()

