from prompto.type.NativeType import NativeType

class BooleanType(NativeType):

    instance = None

    def __init__(self):
        super(BooleanType, self).__init__("Boolean")

    def isAssignableTo(self, context, other):
        from prompto.type.AnyType import AnyType
        return isinstance(other, BooleanType) or isinstance(other, AnyType)

    def sort(self, context, source, desc):
        return sorted(source, reverse=desc)

    def convertPythonValueToPromptoValue(self, context, value, returnType):
        from prompto.value.Boolean import Boolean
        if isinstance(value, bool):
            return Boolean.ValueOf(value)
        else:
            return value  # TODO for now


BooleanType.instance = BooleanType()

