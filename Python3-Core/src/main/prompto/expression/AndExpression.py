from prompto.expression.IExpression import IExpression
from prompto.type.BooleanType import BooleanType
from prompto.value.BooleanValue import BooleanValue
from prompto.error.SyntaxError import SyntaxError
from prompto.utils.CodeWriter import CodeWriter
from prompto.parser.Dialect import Dialect

class AndExpression ( IExpression ):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.left) + " and " + str(self.right)

    def toDialect(self, writer):
        self.left.toDialect(writer)
        writer.append(self.operatorToDialect(writer.dialect))
        self.right.toDialect(writer)

    def operatorToDialect(self, dialect):
        if dialect is Dialect.E or dialect is Dialect.M:
            return " and "
        else:
            return " && "

    def check(self, context):
        lt = self.left.check(context)
        rt = self.right.check(context)
        if not isinstance(lt, BooleanType) or not isinstance(rt, BooleanType):
            raise SyntaxError("Cannot combine " + lt.typeName + " and " + rt.typeName)
        return BooleanType.instance

    def interpret(self, context):
        lval = self.left.interpret(context)
        if not isinstance(lval, BooleanValue):
            raise SyntaxError("Illegal: " + type(lval).__name__ + " and ..., expected a Boolean ")
        if lval is BooleanValue.FALSE:
            return lval
        rval = self.right.interpret(context)
        if not isinstance(rval, BooleanValue):
            raise SyntaxError("Illegal: Boolean and " + type(rval).__name__)
        return rval

    def interpretAssert(self, context, test):
        lval = self.left.interpret(context)
        if not isinstance(lval, BooleanValue):
            raise SyntaxError("Illegal: " + type(lval).__name__ + " and ..., expected a Boolean ")
        rval = lval
        if lval is BooleanValue.TRUE:
            rval = self.right.interpret(context)
        if rval is BooleanValue.TRUE:
            return True
        writer = CodeWriter(test.dialect, context)
        self.toDialect(writer)
        expected = str(writer)
        actual = str(lval) + self.operatorToDialect(test.dialect) + str(rval)
        test.printFailedAssertion(context, expected, actual)
        return False
