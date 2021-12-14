from prompto.expression.FetchOneExpression import FetchOneExpression


class FetchOneStatement(FetchOneExpression):

    def __init__(self, typ, predicate, include, thenWith):
        super().__init__(typ, predicate, include)
        self.thenWith = thenWith


    def canReturn(self):
        return False


    def isSimple(self):
        return False


    def check(self, context):
        super().check(context)
        return self.thenWith.check(context, self.typ)


    def interpret(self, context):
        record = super().interpret(context)
        return self.thenWith.interpret(context, record)


    def toDialect(self, writer):
        super().toDialect(writer)
        self.thenWith.toDialect(writer, self.typ)

