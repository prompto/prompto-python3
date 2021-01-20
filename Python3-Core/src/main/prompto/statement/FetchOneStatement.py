from prompto.expression.FetchOneExpression import FetchOneExpression
from prompto.parser.Dialect import Dialect
from prompto.runtime.Variable import Variable
from prompto.type.VoidType import VoidType


class FetchOneStatement(FetchOneExpression):

    def __init__(self, typ, predicate, thenWith):
        super().__init__(typ, predicate)
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

