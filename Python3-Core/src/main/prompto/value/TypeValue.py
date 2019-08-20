from prompto.type.IType import IType
from prompto.type.TypeType import TypeType
from prompto.value.BaseValue import BaseValue


class TypeValue(BaseValue):

    def __init__(self, value:IType):
        super().__init__(TypeType(value))
        self.value = value


    def getMemberValue(self, context, name, autoCreate=False):
        return self.value.getStaticMemberValue(context, name)


    def __str__(self):
        return self.value.typeName