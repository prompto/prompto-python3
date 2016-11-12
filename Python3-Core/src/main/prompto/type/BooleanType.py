from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily



class BooleanType(NativeType):

    instance = None

    def __init__(self):
        super(BooleanType, self).__init__(TypeFamily.BOOLEAN)

    def sort(self, context, source, desc):
        return sorted(source, reverse=desc)

    def convertPythonValueToPromptoValue(self, context, value, returnType):
        if isinstance(value, bool):
            from prompto.value.Boolean import Boolean
            return Boolean.ValueOf(value)
        else:
            return value  # TODO for now


BooleanType.instance = BooleanType()

