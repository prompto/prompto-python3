from prompto.declaration.BuiltInMethodDeclaration import BuiltInMethodDeclaration
from prompto.type.BooleanType import BooleanType
from prompto.type.IterableType import IterableType
from prompto.type.TextType import TextType


class ContainerType ( IterableType ) :

    def __init__(self, family, itemType):
        super().__init__(family, itemType)

    def checkContains(self, context, other):
        if other.isAssignableFrom(context, self.itemType):
            return BooleanType.instance
        else:
            return super(ContainerType, self).checkContains(context, other)


class BaseJoinMethodDeclaration(BuiltInMethodDeclaration):

    def __init__(self):
        from prompto.param.CategoryParameter import CategoryParameter
        DELIMITER_ARGUMENT = CategoryParameter(TextType.instance, "delimiter")
        super().__init__("join", DELIMITER_ARGUMENT)


    def interpret(self, context):
        from prompto.value.TextValue import TextValue
        items = self.getItems(context)
        items = [str(item) for item in items]
        delimiter = context.getValue("delimiter").value
        joined = delimiter.join(items)
        return TextValue(joined)


    def check(self, context, isStart=False):
        from prompto.type.BooleanType import BooleanType
        return BooleanType.instance
