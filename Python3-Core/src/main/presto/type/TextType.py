from presto.type.NativeType import NativeType


class TextType(NativeType):
    instance = None

    def __init__(self):
        super(TextType, self).__init__("Text")

    def isAssignableTo(self, context, other):
        from presto.type.AnyType import AnyType
        return isinstance(other, TextType) or isinstance(other, AnyType)

    def checkAdd(self, context, other, tryReverse):
        return self

    def checkMultiply(self, context, other, tryReverse):
        from presto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return self
        else:
            return super(TextType, self).checkMultiply(context, other, tryReverse)

    def checkCompare(self, context, other):
        from presto.type.BooleanType import BooleanType
        from presto.type.CharacterType import CharacterType
        if isinstance(other, TextType) or isinstance(other, CharacterType):
            return BooleanType.instance
        return super(TextType, self).checkCompare(context, other)


    def checkItem(self, context, other):
        from presto.type.IntegerType import IntegerType
        from presto.type.CharacterType import CharacterType
        if other == IntegerType.instance:
            return CharacterType.instance
        else:
            return super(TextType, self).checkItem(context, other)


    def checkMember(self, context, name):
        from presto.type.IntegerType import IntegerType
        if "length" == name:
            return IntegerType.instance
        else:
            return super(TextType, self).checkMember(context, name)


    def checkContains(self, context, other):
        from presto.type.BooleanType import BooleanType
        from presto.type.CharacterType import CharacterType
        if isinstance(other, TextType) or isinstance(other, CharacterType):
            return BooleanType.instance
        return super(TextType, self).checkContains(context, other)


    def checkContainsAllOrAny(self, context, other):
        from presto.type.BooleanType import BooleanType
        return BooleanType.instance


    def checkSlice(self, context):
        return self


    def sort(self, context, list_):
        return sorted(list_)


    def convertPythonValueToPrestoValue(self, context, value, returnType):
        from presto.value.Text import Text
        if isinstance(value, str):
            return Text(value)
        else:
            return value  # TODO for now


TextType.instance = TextType()