from datetime import time

from prompto.literal.Literal import Literal
from prompto.type.TimeType import TimeType
from prompto.value.Time import Time


class TimeLiteral(Literal):
    def __init__(self, text):
        value = Time.Parse(text[1:-1])
        super(TimeLiteral, self).__init__(text, value)

    def check(self, context):
        return TimeType.instance
	