from prompto.expression.IExpression import IExpression
from prompto.expression.InstanceExpression import InstanceExpression
from prompto.expression.UnresolvedIdentifier import UnresolvedIdentifier
from prompto.grammar.CmpOp import CmpOp
from prompto.store.InvalidValueError import InvalidValueError
from prompto.store.MatchOp import MatchOp
from prompto.value.Boolean import Boolean
from prompto.value.IInstance import IInstance
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
        actual = str(lval) + " " + str(self.operator) + " " + str(rval)
        test.printFailure(context, expected, actual)
        return False


    def interpretQuery(self, context, query):
        name = None
        value = None
        if isinstance(self.left, (UnresolvedIdentifier, InstanceExpression)):
            name = self.left.name
            value = self.right.interpret(context)
        elif isinstance(self.right, (UnresolvedIdentifier, InstanceExpression)):
            name = self.right.name
            value = self.left.interpret(context)
        if name is None:
            raise SyntaxError("Unable to interpret predicate")
        else:
            decl = context.findAttribute(name)
            info = None if decl is None else decl.getAttributeInfo()
            if isinstance(value, IInstance):
                value = value.getMemberValue(context, "dbId", False)
            matchOp = self.getMatchOp()
            query.verify(info, matchOp, None if value is None else value.getStorableData())
            if self.operator in [CmpOp.GTE, CmpOp.LTE]:
                query.Not()

    def getMatchOp(self):
        if self.operator in [CmpOp.GT, CmpOp.LTE]:
            return MatchOp.GREATER
        elif self.operator in [CmpOp.GTE, CmpOp.LT]:
            return MatchOp.LESSER
        else:
            raise InvalidValueError(str(self.operator))