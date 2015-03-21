from presto.type.CategoryType import CategoryType
from presto.type.TextType import TextType


class EnumeratedCategoryType ( CategoryType ):

    def __init__(self, name):
        super(EnumeratedCategoryType, self).__init__(name)

    def checkMember(self, context, name):
        if "value"==name:
            return self
        elif "name"==name:
            return TextType.instance
        else:
            return super(EnumeratedCategoryType, self).checkMember(context, name)
