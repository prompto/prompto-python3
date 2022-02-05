from prompto.declaration.BuiltInMethodDeclaration import BuiltInMethodDeclaration
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
            return super().checkMultiply(context, other, tryReverse)

    def checkCompare(self, context, other):
        from prompto.type.BooleanType import BooleanType
        from prompto.type.CharacterType import CharacterType
        if isinstance(other, TextType) or isinstance(other, CharacterType):
            return BooleanType.instance
        return super().checkCompare(context, other)


    def checkItem(self, context, other):
        from prompto.type.IntegerType import IntegerType
        from prompto.type.CharacterType import CharacterType
        if other == IntegerType.instance:
            return CharacterType.instance
        else:
            return super().checkItem(context, other)


    def checkMember(self, context, name):
        from prompto.type.IntegerType import IntegerType
        if "count" == name:
            return IntegerType.instance
        else:
            return super().checkMember(context, name)


    def checkContains(self, context, other):
        from prompto.type.BooleanType import BooleanType
        from prompto.type.CharacterType import CharacterType
        if isinstance(other, TextType) or isinstance(other, CharacterType):
            return BooleanType.instance
        return super().checkContains(context, other)


    def checkContainsAllOrAny(self, context, other):
        from prompto.type.BooleanType import BooleanType
        return BooleanType.instance


    def checkSlice(self, context):
        return self


    def convertPythonValueToPromptoValue(self, context, value, returnType):
        from prompto.value.TextValue import TextValue
        if isinstance(value, str):
            return TextValue(value)
        else:
            return super().convertPythonValueToPromptoValue(context, value, returnType)

    def getMemberMethods(self, context, name):
        if name == "startsWith":
            return [StartsWithMethodDeclaration()]
        elif name == "endsWith":
            return [EndsWithMethodDeclaration()]
        elif name == "toLowerCase":
            return [ToLowerCaseMethodDeclaration()]
        elif name == "toUpperCase":
            return [ToUpperCaseMethodDeclaration()]
        elif name == "toCapitalized":
            return [ToCapitalizedMethodDeclaration()]
        elif name == "replace":
            return [ReplaceMethodDeclaration()]
        elif name == "replaceAll":
            return [ReplaceAllMethodDeclaration()]
        elif name == "split":
            return [SplitMethodDeclaration()]
        elif name == "trim":
            return [TrimMethodDeclaration()]
        elif name == "indexOf":
            return [IndexOfMethodDeclaration()]
        else:
            return super().getMemberMethods(context, name)


TextType.instance = TextType()

class StartsWithMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        from prompto.param.CategoryParameter import CategoryParameter
        VALUE_ARGUMENT = CategoryParameter(TextType.instance, "value")
        super().__init__("startsWith", VALUE_ARGUMENT)


    def interpret(self, context):
        from prompto.value.BooleanValue import BooleanValue
        value = self.getValue(context).value
        find = context.getValue("value").value
        startsWith = value.startswith(find)
        return BooleanValue.ValueOf(startsWith)


    def check(self, context):
        from prompto.type.BooleanType import BooleanType
        return BooleanType.instance


class EndsWithMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        from prompto.param.CategoryParameter import CategoryParameter
        VALUE_ARGUMENT = CategoryParameter(TextType.instance, "value")
        super().__init__("endsWith", VALUE_ARGUMENT)


    def interpret(self, context):
        from prompto.value.BooleanValue import BooleanValue
        value = self.getValue(context).value
        find = context.getValue("value").value
        endsWith = value.endswith(find)
        return BooleanValue.ValueOf(endsWith)


    def check(self, context):
        from prompto.type.BooleanType import BooleanType
        return BooleanType.instance




class SplitMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        from prompto.param.CategoryParameter import CategoryParameter
        from prompto.literal.TextLiteral import TextLiteral
        SINGLE_SPACE_ARGUMENT = CategoryParameter(TextType.instance, "separator", TextLiteral('" "'))
        super().__init__("split", SINGLE_SPACE_ARGUMENT)


    def interpret(self, context):
        from prompto.value.TextValue import TextValue
        from prompto.value.ListValue import ListValue
        value = self.getValue(context).value
        sep = context.getValue("separator").value
        parts = [TextValue(part) for part in value.split(sep)]
        return ListValue(TextType.instance, parts, mutable = False)


    def check(self, context):
        from prompto.type.ListType import ListType
        return ListType(TextType.instance)


class ReplaceMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        from prompto.param.CategoryParameter import CategoryParameter
        TO_REPLACE_ARGUMENT = CategoryParameter(TextType.instance, "toReplace")
        REPLACE_WITH_ARGUMENT = CategoryParameter(TextType.instance, "replaceWith")
        super().__init__("replace", TO_REPLACE_ARGUMENT, REPLACE_WITH_ARGUMENT)


    def interpret(self, context):
        from prompto.value.TextValue import TextValue
        value = self.getValue(context).value
        toReplace = context.getValue("toReplace").value
        replaceWith = context.getValue("replaceWith").value
        value = value.replace(toReplace, replaceWith, 1)
        return TextValue(value)


    def check(self, context):
        return TextType.instance


class ReplaceAllMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        from prompto.param.CategoryParameter import CategoryParameter
        TO_REPLACE_ARGUMENT = CategoryParameter(TextType.instance, "toReplace")
        REPLACE_WITH_ARGUMENT = CategoryParameter(TextType.instance, "replaceWith")
        super().__init__("replaceAll", TO_REPLACE_ARGUMENT, REPLACE_WITH_ARGUMENT)


    def interpret(self, context):
        from prompto.value.TextValue import TextValue
        value = self.getValue(context).value
        toReplace = context.getValue("toReplace").value
        replaceWith = context.getValue("replaceWith").value
        value = value.replace(toReplace, replaceWith)
        return TextValue(value)


    def check(self, context):
        return TextType.instance

class ToLowerCaseMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        super().__init__("toLowerCase")


    def interpret(self, context):
        from prompto.value.TextValue import TextValue
        value = self.getValue(context).getStorableData()
        return TextValue(value.lower())


    def check(self, context):
        return TextType.instance



class ToUpperCaseMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        super().__init__("toUpperCase")


    def interpret(self, context):
        from prompto.value.TextValue import TextValue
        value = self.getValue(context).getStorableData()
        return TextValue(value.upper())


    def check(self, context):
        return TextType.instance



class ToCapitalizedMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        super().__init__("toCapitalized")


    def interpret(self, context):
        from prompto.value.TextValue import TextValue
        value = self.getValue(context).getStorableData()
        return TextValue(value.title())


    def check(self, context):
        return TextType.instance


class TrimMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        super().__init__("trim")


    def interpret(self, context):
        from prompto.value.TextValue import TextValue
        value = self.getValue(context).getStorableData()
        return TextValue(value.strip())


    def check(self, context):
        return TextType.instance


class IndexOfMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        from prompto.param.CategoryParameter import CategoryParameter
        VALUE_ARGUMENT = CategoryParameter(TextType.instance, "value")
        from prompto.type.IntegerType import IntegerType
        from prompto.literal.IntegerLiteral import IntegerLiteral
        FROM_INDEX_ARGUMENT = CategoryParameter(IntegerType.instance, "fromIndex", IntegerLiteral("1"))
        super().__init__("indexOf", VALUE_ARGUMENT, FROM_INDEX_ARGUMENT)


    def interpret(self, context):
        from prompto.value.IntegerValue import IntegerValue
        value = self.getValue(context).value
        toFind = context.getValue("value").value
        fromIndex = context.getValue("fromIndex").value
        index = value.index(toFind, fromIndex - 1)
        return IntegerValue(index + 1)


    def check(self, context):
        from prompto.type.IntegerType import IntegerType
        return IntegerType.instance


