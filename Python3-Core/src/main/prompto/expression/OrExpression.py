from prompto.expression.IExpression import IExpression
from prompto.type.BooleanType import BooleanType
from prompto.value.BooleanValue import BooleanValue
from prompto.error.SyntaxError import SyntaxError
from prompto.utils.CodeWriter import CodeWriter
from prompto.parser.Dialect import Dialect

class OrExpression ( IExpression ):

    def __init__(self, left, right):
        self.left = left
        self.right = right


    def __str__(self):
        return str(self.left) + " or " + str(self.right)

    def toDialect(self, writer):
        self.left.toDialect(writer)
        writer.append(self.operatorToDialect(writer.dialect))
        self.right.toDialect(writer)

    def operatorToDialect(self, dialect):
        if dialect is Dialect.E or dialect is Dialect.M:
            return " or "
        else:
            return " || "

    def check(self, context):
        lt = self.left.check(context)
        rt = self.right.check(context)
        if not isinstance(lt, BooleanType) or not isinstance(rt, BooleanType):
            raise SyntaxError("Cannot combine " + lt.getName() + " and " + rt.getName())
        return BooleanType.instance

    def interpret(self, context):
        lval = self.left.interpret(context)
        rval = self.right.interpret(context)
        return self.interpretValue(context, lval, rval)

    def interpretValue(self, context, lval, rval):
        if isinstance(lval, BooleanValue):
            if isinstance(rval, BooleanValue):
                return BooleanValue.ValueOf(lval.getValue() or rval.getValue())
            else:
                raise SyntaxError("Illegal: Boolean and " + type(rval).__name__)
        else:
            raise SyntaxError("Illegal: " + type(lval).__name__ + " + " + type(rval).__name__)

    def interpretAssert(self, context, test):
        lval = self.left.interpret(context)
        rval = self.right.interpret(context)
        result = self.interpretValue(context, lval, rval)
        if result is BooleanValue.TRUE:
            return True
        writer = CodeWriter(test.dialect, context)
        self.toDialect(writer)
        expected = str(writer)
        actual = str(lval) + self.operatorToDialect(test.dialect) + str(rval)
        test.printFailedAssertion(context, expected, actual)
        return False


    def interpretQuery(self, context, query):
        if getattr(self.left, "interpretQuery", None) is None:
            raise SyntaxError("Not a predicate: " + str(self.left))
        self.left.interpretQuery(context, query)
        if getattr(self.right, "interpretQuery", None) is None:
            raise SyntaxError("Not a predicate: " + str(self.right))
        self.right.interpretQuery(context, query)
        query.Or()

