from presto.expression.IExpression import IExpression


class ParenthesisExpression ( IExpression ):

    def __init__(self, expression):
        super(ParenthesisExpression, self).__init__()
        self.expression = expression

    def __str__(self):
        return "(" + str(self.expression) + ")"

    def toDialect(self, writer):
        writer.append("(")
        self.expression.toDialect(writer)
        writer.append(")")

    def check(self, context):
        return self.expression.check(context)

    def interpret(self, context):
        return self.expression.interpret(context)
