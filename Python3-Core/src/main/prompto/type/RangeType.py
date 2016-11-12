from prompto.store.TypeFamily import TypeFamily
from prompto.type.ContainerType import ContainerType

class RangeType(ContainerType):

    def __init__(self, itemType):
        super(RangeType, self).__init__(TypeFamily.RANGE, itemType)
        self.typeName = itemType.typeName + "[..]"


    def __eq__(self, obj):
        if id(obj) == id(self):
            return True
        if obj == None:
            return False
        if not isinstance(obj, RangeType):
            return False
        return self.getItemType() == obj.getItemType()

    def checkItem(self, context, other):
        from prompto.type.IntegerType import IntegerType
        if other == IntegerType.instance:
            return self.itemType
        else:
            return super().checkItem(context, other)


    def checkSlice(self, context):
        return self


    def checkIterator(self, context):
        return self.itemType


    def checkContainsAllOrAny(self, context, other):
        from prompto.type.BooleanType import BooleanType
        return BooleanType.instance
