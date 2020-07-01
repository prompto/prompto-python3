from prompto.expression.InstanceExpression import InstanceExpression
from prompto.value.TextValue import TextValue
from prompto.error.SyntaxError import SyntaxError


class DictIdentifierKey(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interpret(self, context):
        value = InstanceExpression(self.name).interpret(context)
        if isinstance(value, TextValue):
            return value
        else:
            raise SyntaxError("Expecting a Text, got a " + value.itype.typename)
