from prompto.value.BaseValue import BaseValue


class BooleanValue(BaseValue):
    TRUE = None
    FALSE = None

    @staticmethod
    def Parse(text):
        return BooleanValue.TRUE if text == "true" else BooleanValue.FALSE


    @staticmethod
    def ValueOf(value):
        return BooleanValue.TRUE if value else BooleanValue.FALSE


    def __init__(self, value):
        from prompto.type.BooleanType import BooleanType
        super().__init__(BooleanType.instance)
        self.value = value

    def getStorableData(self):
        return self.value


    def getValue(self):
        return self.value


    def getNot(self):
        return self.opposite


    def __str__(self):
        return str(self.value).lower()


    def __eq__(self, obj):
        if isinstance(obj, BooleanValue):
            return self.value == obj.value
        else:
            return False


    def __lt__(self, obj):
        return self.value < obj.value


    def __hash__(self):
        return hash(self.value)


    def toJsonNode(self):
        return self.value

BooleanValue.TRUE = BooleanValue(True)
BooleanValue.FALSE = BooleanValue(False)
BooleanValue.TRUE.opposite = BooleanValue.FALSE
BooleanValue.FALSE.opposite = BooleanValue.TRUE