from prompto.type.NullType import NullType
from prompto.value.BaseValue import BaseValue


class NullValue (BaseValue):

    instance = None

    def __init__(self):
        super().__init__(NullType.instance)


    def convertToPython(self):
        return None


    def getStorableData(self):
        return None # Yes!


    def toJsonNode(self):
        return None


    def __str__(self):
        return "null"

NullValue.instance = NullValue()
