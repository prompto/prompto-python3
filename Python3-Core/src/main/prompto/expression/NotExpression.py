from prompto.expression.IUnaryExpression import IUnaryExpression
from prompto.type.BooleanType import BooleanType
from prompto.value.Boolean import Boolean
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
        type_ = self.expression.check(context)
        if not isinstance(type_, BooleanType):
            raise SyntaxError("Cannot negate " + type_.getName())
        return BooleanType.instance

    def interpret(self, context):
        val = self.expression.interpret(context)
        return self.interpretValue(context, val)

    def interpretValue(self, context, val):
        if isinstance(val, Boolean):
            return val.getNot()
        else:
            raise SyntaxError("Illegal: not " + type(val).__name__)

    def interpretAssert(self, context, test):
        val = self.expression.interpret(context)
        result = self.interpretValue(context, val)
        if result is Boolean.TRUE:
            return True
        writer = CodeWriter(test.dialect, context)
        self.toDialect(writer)
        expected = str(writer)
        actual = self.operatorToDialect(test.dialect) + str(val)
        test.printFailure(context, expected, actual)
        return False
