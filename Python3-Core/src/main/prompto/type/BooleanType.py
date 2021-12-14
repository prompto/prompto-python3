from prompto.type.NativeType import NativeType
from prompto.store.TypeFamily import TypeFamily



class BooleanType(NativeType):

    instance = None

    def __init__(self):
        super(BooleanType, self).__init__(TypeFamily.BOOLEAN)


    def convertPythonValueToPromptoValue(self, context, value, returnType):
        if isinstance(value, bool):
            from prompto.value.BooleanValue import BooleanValue
            return BooleanValue.ValueOf(value)
        else:
            return super().convertPythonValueToPromptoValue(context, value, returnType)  # TODO for now


BooleanType.instance = BooleanType()

