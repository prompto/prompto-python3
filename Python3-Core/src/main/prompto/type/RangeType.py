from prompto.type.CollectionType import CollectionType

class RangeType(CollectionType):
    def __init__(self, itemType):
        super(RangeType, self).__init__(itemType.getName() + "[..]", itemType)

    def isAssignableTo(self, context, other):
        return self == other

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
