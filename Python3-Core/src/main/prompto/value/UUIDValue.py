from prompto.value.BaseValue import BaseValue


class UUIDValue ( BaseValue) :

    def __init__(self, value):
        from prompto.type.UUIDType import UUIDType
        super(UUIDValue, self).__init__(UUIDType.instance)
        self.value = value

    def convertToPython(self):
        return self.value

    def getValue(self):
        return self.value
 
    def __str__(self):
        return str(self.value)
 
    def __eq__(self, obj):
        if isinstance(obj, UUIDValue):
            return self.value == obj.value
        else:
            return self.value == obj

    def __hash__(self):
        return hash(self.value)


    def toDocumentValue(self, context):
        from prompto.value.TextValue import TextValue
        return TextValue(str(self))


    def toJsonNode(self):
        return str(self.value)
