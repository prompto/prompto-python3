from presto.type.BaseType import BaseType


class NullType(BaseType):

    instance = None

    def __init__(self):
        super(NullType, self).__init__("Null")

    def isAssignableTo (self, context,  other):
        return True

    def isMoreSpecificThan (self, context, other):
        return False

NullType.instance = NullType()
