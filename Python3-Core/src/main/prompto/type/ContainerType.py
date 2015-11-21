from prompto.type.BooleanType import BooleanType
from prompto.type.IterableType import IterableType


class ContainerType ( IterableType ) :

    def __init__(self, name, itemType):
        super().__init__(name, itemType)

    def checkContains(self, context, other):
        if self.itemType.isAssignableTo(context, other):
            return BooleanType.instance
        else:
            return super(ContainerType, self).checkContains(context, other)
