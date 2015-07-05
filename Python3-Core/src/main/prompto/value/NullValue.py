from prompto.type.NullType import NullType
from prompto.value.BaseValue import BaseValue


class NullValue (BaseValue):

    instance = None

    def __init__(self):
        super().__init__(NullType.instance)

NullValue.instance = NullValue()
