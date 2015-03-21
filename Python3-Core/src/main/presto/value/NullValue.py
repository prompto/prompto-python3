from presto.type.NullType import NullType
from presto.value.BaseValue import BaseValue


class NullValue (BaseValue):

    instance = None

    def __init__(self):
        super().__init__(NullType.instance)

NullValue.instance = NullValue()
