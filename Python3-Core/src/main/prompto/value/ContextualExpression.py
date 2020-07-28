from prompto.expression.IExpression import IExpression
from prompto.value.BaseValue import BaseValue
from prompto.type.MissingType import MissingType


class ContextualExpression(BaseValue, IExpression):

    def __init__(self, calling, expression):
        super(ContextualExpression, self).__init__(MissingType.instance) # TODO check that this is not a problem
        self.calling = calling
        self.expression = expression


    def __str__(self):
        return str(self.expression)


    def check(self, context):
        return self.expression.check(self.calling)


    def checkReference(self, context):
        return self.expression.checkReference(self.calling)


    def interpret(self, context):
        return self.expression.interpret(self.calling)


    def interpretReference(self, context):
        return self.expression.interpretReference(self.calling)
