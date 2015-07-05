from prompto.type.IType import IType
from prompto.type.MissingType import MissingType
from prompto.value.BaseValue import BaseValue


class TypeValue(BaseValue):

    def __init__(self, value:IType):
        super().__init__(MissingType.instance)  # TODO check that this is ok
        self.value = value
