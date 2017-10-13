from prompto.value.BaseValue import BaseValue
from prompto.expression.IExpression import IExpression


class ExpressionValue(BaseValue, IExpression):

    def __init__(self, type, value):
        super().__init__(type)
        self.value = value

    def check(self, context):
        return self.itype

    def interpret(self, context):
        if isinstance(self.value, IExpression):
            return self.value.interpret(context)
        else:
            return self.value

    def __str__(self):
        return str(self.value)
