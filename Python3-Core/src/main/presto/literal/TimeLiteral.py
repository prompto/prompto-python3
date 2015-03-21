from datetime import time

from presto.literal.Literal import Literal
from presto.type.TimeType import TimeType
from presto.value.Time import Time


class TimeLiteral(Literal):
    def __init__(self, text):
        value = Time.Parse(text[1:-1])
        super(TimeLiteral, self).__init__(text, value)

    def check(self, context):
        return TimeType.instance
	