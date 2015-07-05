from prompto.value.BaseValue import BaseValue


class Boolean(BaseValue):
    TRUE = None
    FALSE = None

    @staticmethod
    def Parse(text):
        return Boolean.TRUE if text == "true" else Boolean.FALSE

    @staticmethod
    def ValueOf(value):
        return Boolean.TRUE if value else Boolean.FALSE

    def __init__(self, value):
        from prompto.type.BooleanType import BooleanType
        super().__init__(BooleanType.instance)
        self.value = value

    def getValue(self):
        return self.value

    def getNot(self):
        return self.opposite

    def __str__(self):
        return str(self.value).lower()

    def __eq__(self, obj):
        if isinstance(obj, Boolean):
            return self.value == obj.value
        else:
            return False

    def __lt__(self, obj):
        return self.value < obj.value

    def __hash__(self):
        return hash(self.value)

Boolean.TRUE = Boolean(True)
Boolean.FALSE = Boolean(False)
Boolean.TRUE.opposite = Boolean.FALSE
Boolean.FALSE.opposite = Boolean.TRUE