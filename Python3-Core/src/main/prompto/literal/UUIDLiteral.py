from prompto.literal.Literal import Literal
from uuid import UUID

class UUIDLiteral(Literal):

    def __init__(self, text):
        from prompto.value.UUIDValue import UUIDValue
        value = UUIDValue(UUID(text[1:-1]))
        super(UUIDLiteral, self).__init__(text, value)

    def check(self, context):
        from prompto.type.UUIDType import UUIDType
        return UUIDType.instance
