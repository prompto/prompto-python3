from prompto.type.BooleanType import BooleanType
from prompto.type.IterableType import IterableType


class ContainerType ( IterableType ) :

    def __init__(self, family, itemType):
        super().__init__(family, itemType)

    def checkContains(self, context, other):
        if other.isAssignableFrom(context, self.itemType):
            return BooleanType.instance
        else:
            return super(ContainerType, self).checkContains(context, other)
