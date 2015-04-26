from presto.expression.IExpression import IExpression
from presto.type.CodeType import CodeType
from presto.value.CodeValue import CodeValue

class CodeExpression ( IExpression ):

    def __init__(self, expression):
        super(CodeExpression, self).__init__()
        self.expression = expression

    def __str__(self):
        return "Code: " + str(self.expression)

    def toEDialect(self, writer):
        writer.append("Code: ")
        self.expression.toDialect(writer)

    def toODialect(self, writer):
        writer.append("Code(")
        self.expression.toDialect(writer)
        writer.append(")")

    def toSDialect(self, writer):
        self.toODialect(writer)

    def check(self, context):
        return CodeType.instance

    def interpret(self, context):
        return CodeValue(self)

    # expression can only be checked and evaluated in the context of an execute:
    def checkCode(self, context):
        return self.expression.check(context)

    def interpretCode(self, context):
        return self.expression.interpret(context)

