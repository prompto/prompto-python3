from prompto.expression.IExpression import IExpression


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


    def checkQuery(self, context):
        if getattr(self.expression, "checkQuery", None) is None:
            raise SyntaxError("Not a predicate: " + str(self.expression))
        self.expression.checkQuery(context)


    def interpretQuery(self, context, query):
        if getattr(self.expression, "interpretQuery", None) is None:
            raise SyntaxError("Not a predicate: " + str(self.expression))
        self.expression.interpretQuery(context, query)
