from prompto.value.BaseValue import BaseValue
from prompto.type.CodeType import CodeType

class CodeValue(BaseValue):

    def __init__(self, expression):
        super().__init__(CodeType.instance)
        self.expression = expression

    def check(self, context):
        return self.expression.checkCode(context)

    def interpret(self, context):
        return self.expression.interpretCode(context)