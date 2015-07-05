from prompto.expression.IExpression import IExpression
from prompto.grammar.CmpOp import CmpOp
from prompto.value.Boolean import Boolean
from prompto.value.IValue import IValue
from prompto.utils.CodeWriter import CodeWriter
from prompto.error.SyntaxError import SyntaxError

class CompareExpression ( IExpression ):

    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self):
        return str(self.left) + " " + str(self.operator) + " " + str(self.right)

    def toDialect(self, writer):
        self.left.toDialect(writer)
        writer.append(" ")
        self.operator.toDialect(writer)
        writer.append(" ")
        self.right.toDialect(writer)

    def check(self, context):
        lt = self.right.check(context)
        rt = self.right.check(context)
        return lt.checkCompare(context,rt)

    def interpret(self, context):
        lval = self.left.interpret(context)
        rval = self.right.interpret(context)
        if isinstance(lval, IValue) and isinstance(rval, IValue):
            return self.compare(context, lval, rval)
        else:
            raise SyntaxError("Illegal comparison: " + type(lval).__name__ \
                            + " " + str(self.operator) + " " + type(rval).__name__)

    def compare(self, context, lval, rval):
        cmp = lval.compareTo(context, rval)
        if self.operator==CmpOp.GT:
            return Boolean.ValueOf(cmp > 0)
        elif self.operator==CmpOp.LT:
            return Boolean.ValueOf(cmp < 0)
        elif self.operator==CmpOp.GTE:
            return Boolean.ValueOf(cmp >= 0)
        elif self.operator==CmpOp.LTE:
            return Boolean.ValueOf(cmp <= 0)
        else:
            raise SyntaxError("Illegal compare operand: " + str(self.operator))

    def interpretAssert(self, context, test):
        lval = self.left.interpret(context)
        rval = self.right.interpret(context)
        result = self.compare(context, lval, rval)
        if result is Boolean.TRUE:
            return True
        writer = CodeWriter(test.dialect, context)
        self.toDialect(writer)
        expected = str(writer)
        actual = str(lval) + " " + self.operator.toDialect(test.dialect) + " " + str(rval)
        test.printFailure(context, expected, actual)
        return False
