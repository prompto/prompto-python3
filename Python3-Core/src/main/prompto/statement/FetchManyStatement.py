from prompto.expression.FetchManyExpression import FetchManyExpression
from prompto.parser.Dialect import Dialect
from prompto.runtime.Variable import Variable
from prompto.type.CursorType import CursorType
from prompto.type.VoidType import VoidType


class FetchManyStatement(FetchManyExpression):

    def __init__(self, typ, predicate, first, last, orderBy, thenWith):
        super().__init__(typ,predicate, first, last, orderBy)
        self.thenWith = thenWith


    def canReturn(self):
        return False

    def isSimple(self):
        return False


    def check(self, context):
        super().check(context)
        return self.thenWith.check(context, CursorType(self.typ))


    def interpret(self, context):
        record = super().interpret(context)
        return self.thenWith.interpret(context, record)


    def toDialect(self, writer):
        super().toDialect(writer)
        self.thenWith.toDialect(writer, CursorType(self.typ))

