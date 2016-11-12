from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily



class TextType(NativeType):
    instance = None

    def __init__(self):
        super().__init__(TypeFamily.TEXT)

    def isAssignableFrom(self, context, other):
        from prompto.type.CharacterType import CharacterType
        return super().isAssignableFrom(context, other) or \
               other is CharacterType.instance


    def checkAdd(self, context, other, tryReverse):
        return self

    def checkMultiply(self, context, other, tryReverse):
        from prompto.type.IntegerType import IntegerType
        if isinstance(other, IntegerType):
            return self
        else:
            return super(TextType, self).checkMultiply(context, other, tryReverse)

    def checkCompare(self, context, other):
        from prompto.type.BooleanType import BooleanType
        from prompto.type.CharacterType import CharacterType
        if isinstance(other, TextType) or isinstance(other, CharacterType):
            return BooleanType.instance
        return super(TextType, self).checkCompare(context, other)


    def checkItem(self, context, other):
        from prompto.type.IntegerType import IntegerType
        from prompto.type.CharacterType import CharacterType
        if other == IntegerType.instance:
            return CharacterType.instance
        else:
            return super(TextType, self).checkItem(context, other)


    def checkMember(self, context, name):
        from prompto.type.IntegerType import IntegerType
        if "count" == name:
            return IntegerType.instance
        else:
            return super(TextType, self).checkMember(context, name)


    def checkContains(self, context, other):
        from prompto.type.BooleanType import BooleanType
        from prompto.type.CharacterType import CharacterType
        if isinstance(other, TextType) or isinstance(other, CharacterType):
            return BooleanType.instance
        return super(TextType, self).checkContains(context, other)


    def checkContainsAllOrAny(self, context, other):
        from prompto.type.BooleanType import BooleanType
        return BooleanType.instance


    def checkSlice(self, context):
        return self


    def sort(self, context, list_, desc):
        return sorted(list_, reverse=desc)


    def convertPythonValueToPromptoValue(self, context, value, returnType):
        from prompto.value.Text import Text
        if isinstance(value, str):
            return Text(value)
        else:
            return value  # TODO for now


TextType.instance = TextType()