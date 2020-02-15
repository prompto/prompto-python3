from prompto.literal.Literal import Literal
from prompto.value.IntegerValue import IntegerValue


class IntegerLiteral(Literal):

    def __init__(self, text, value = None):
        value = IntegerValue(int(text)) if value is None else value
        super(IntegerLiteral, self).__init__(text, value)

    def check(self, context):
        from prompto.type.IntegerType import IntegerType
        return IntegerType.instance

class MinIntegerLiteral(IntegerLiteral):

    def __init__(self):
        super(MinIntegerLiteral, self).__init__("MIN_INTEGER", IntegerValue(-pow(2, 63) - 1))

class MaxIntegerLiteral(IntegerLiteral):

    def __init__(self):
        super(MaxIntegerLiteral, self).__init__("MAX_INTEGER", IntegerValue(pow(2, 63)))
