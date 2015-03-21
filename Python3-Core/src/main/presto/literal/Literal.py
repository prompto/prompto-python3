from presto.expression.IExpression import IExpression


class Literal (IExpression):

    def __init__(self, text, value):
        super(Literal, self).__init__()
        self.text = text
        self.value = value

    def toDialect(self, writer):
        writer.append(self.text)

    def __str__(self):
        return self.text

    def getValue(self):
        return self.value

    def interpret(self, context):
        return self.value
