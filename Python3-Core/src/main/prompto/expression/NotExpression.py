from prompto.expression.IUnaryExpression import IUnaryExpression
from prompto.type.BooleanType import BooleanType
from prompto.value.BooleanValue import BooleanValue
from prompto.error.SyntaxError import SyntaxError
from prompto.utils.CodeWriter import CodeWriter
from prompto.parser.Dialect import Dialect

class NotExpression ( IUnaryExpression ):

    def __init__(self, expression):
        self.expression = expression


    def __str__(self):
        return "not " + str(self.expression)


    def toDialect(self, writer):
        writer.append(self.operatorToDialect(writer.dialect))
        self.expression.toDialect(writer)


    def operatorToDialect(self, dialect):
        if dialect is Dialect.E or dialect is Dialect.M:
            return "not "
        else:
            return "!"


    def check(self, context):
        itype = self.expression.check(context)
        if not isinstance(itype, BooleanType):
            raise SyntaxError("Cannot negate " + itype.getName())
        return BooleanType.instance


    def checkQuery(self, context):
        if getattr(self.expression, "checkQuery", None) is None:
            raise SyntaxError("Not a predicate: " + str(self.expression))
        self.expression.checkQuery(context)


    def interpret(self, context):
        val = self.expression.interpret(context)
        return self.interpretValue(context, val)


    def interpretValue(self, context, val):
        if isinstance(val, BooleanValue):
            return val.getNot()
        else:
            raise SyntaxError("Illegal: not " + type(val).__name__)


    def interpretAssert(self, context, test):
        val = self.expression.interpret(context)
        result = self.interpretValue(context, val)
        if result is BooleanValue.TRUE:
            return True
        writer = CodeWriter(test.dialect, context)
        self.toDialect(writer)
        expected = str(writer)
        actual = self.operatorToDialect(test.dialect) + str(val)
        test.printFailedAssertion(context, expected, actual)
        return False


    def interpretQuery(self, context, query):
        if getattr(self.expression, "interpretQuery", None) is None:
            raise SyntaxError("Not a predicate: " + str(self.expression))
        self.expression.interpretQuery(context, query)
        query.Not()
