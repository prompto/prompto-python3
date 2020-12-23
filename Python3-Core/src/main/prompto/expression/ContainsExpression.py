from prompto.expression.IExpression import IExpression
from prompto.expression.PredicateExpression import PredicateExpression
from prompto.grammar.ContOp import ContOp
from prompto.store.MatchOp import MatchOp
from prompto.type.IterableType import IterableType
from prompto.value.BooleanValue import BooleanValue
from prompto.value.IContainer import IContainer
from prompto.utils.CodeWriter import CodeWriter
from prompto.value.IInstance import IInstance
from prompto.value.IValue import IValue
from prompto.error.SyntaxError import SyntaxError
from prompto.value.NullValue import NullValue


class ContainsExpression(IExpression):

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
        if isinstance(self.right, PredicateExpression):
            return self.checkPredicate(context)
        else:
            return self.checkValue(context)


    def checkPredicate(self, context):
        lt = self.left.check(context)
        if isinstance(lt, IterableType):
            itemType = lt.itemType
            arrow = self.right.toArrowExpression()
            return arrow.checkFilter(context, itemType)
        else:
            raise SyntaxError("Expecting collection")


    def checkValue(self, context):
        lt = self.left.check(context)
        rt = self.right.check(context)
        return self.checkOperator(context, lt, rt)


    def checkOperator(self, context, lt, rt):
        if self.operator in [ContOp.IN, ContOp.NOT_IN]:
            return rt.checkContains(context, lt)
        elif self.operator in [ContOp.HAS, ContOp.NOT_HAS]:
            return lt.checkContains(context, rt)
        else:
            return lt.checkContainsAllOrAny(context, rt)


    def interpret(self, context):
        lval = self.left.interpret(context)
        rval = self.right.interpret(context)
        return self.interpretValue(context, lval, rval)


    def interpretValue(self, context, lval, rval):
        if isinstance(lval, IValue) and isinstance(rval, IValue):
            result = None
            if self.operator in [ContOp.IN, ContOp.NOT_IN]:
                if rval is NullValue.instance:
                    result = False
                elif isinstance(rval, IContainer):
                    result = rval.hasItem(context, lval)
            elif self.operator in [ContOp.HAS, ContOp.NOT_HAS]:
                if lval is NullValue.instance:
                    result = False
                elif isinstance(lval, IContainer):
                    result = lval.hasItem(context, rval)
            elif self.operator in [ContOp.HAS_ALL, ContOp.NOT_HAS_ALL]:
                if lval is NullValue.instance or rval is NullValue.instance:
                    result = False
                elif isinstance(lval, IContainer) and isinstance(rval, IContainer):
                    result = self.containsAll(context, lval, rval)
            elif self.operator in [ContOp.HAS_ANY, ContOp.NOT_HAS_ANY]:
                if lval is NullValue.instance or rval is NullValue.instance:
                    result = False
                elif isinstance(lval, IContainer) and isinstance(rval, IContainer):
                    result = self.containsAny(context, lval, rval)
            if result is not None:
                if self.operator.name.find("NOT") == 0:
                    result = not result
                return BooleanValue.ValueOf(result)
        #prepare exception
        if self.operator.name.find("IN") >= 0:
            tmp = lval
            lval = rval
            rval = tmp
        lowerName = self.operator.name.lower().replace('_', ' ')
        raise SyntaxError("Illegal comparison: " + type(lval).__name__ + \
                          " " + lowerName + " " + type(rval).__name__)


    def containsAll(self, context, container, items):
        for item in items.getIterator(context):
            if isinstance(item, IExpression):
                item = item.interpret(context)
            if isinstance(item, IValue):
                if not container.hasItem(context, item):
                    return False
            else:
                raise SyntaxError("Illegal contain: Text + " + type(item).__name__)
        return True


    def containsAny(self, context, container, items):
        for item in items.getIterator(context):
            if isinstance(item, IExpression):
                item = item.interpret(context)
            if isinstance(item, IValue):
                if container.hasItem(context, item):
                    return True
            else:
                raise SyntaxError("Illegal contain: Text + " + type(item).__name__)
        return False


    def interpretAssert(self, context, test):
        lval = self.left.interpret(context)
        rval = self.right.interpret(context)
        result = self.interpretValue(context, lval, rval)
        if result is BooleanValue.TRUE:
            return True
        writer = CodeWriter(test.dialect, context)
        self.toDialect(writer)
        expected = str(writer)
        writer = CodeWriter(test.dialect, context)
        self.operator.toDialect(writer)
        actual = str(lval) + " " + str(writer) + " " + str(rval)
        test.printFailedAssertion(context, expected, actual)
        return False


    def checkQuery(self, context):
        decl = self.left.checkAttribute(context)
        if not decl.storable:
            raise SyntaxError(decl.name + " is not storable")
        rt = self.right.check(context)
        return self.checkOperator(context, decl.getType(), rt)


    def interpretQuery(self, context, query):
        decl = self.left.checkAttribute(context)
        if decl is None or not decl.storable:
            raise SyntaxError("Unable to interpret predicate")
        value = self.right.interpret(context)
        matchOp = self.getMatchOp(context, decl.getType(), value.itype, self.operator)
        if isinstance(value, IInstance):
            value = value.getMemberValue(context, "dbId", False)
        info = decl.getAttributeInfo()
        data = None if value is None else value.getStorableData()
        query.verify(info, matchOp, data)
        if self.operator in [ContOp.NOT_IN, ContOp.NOT_HAS, ContOp.NOT_HAS_ALL, ContOp.NOT_HAS_ANY]:
            query.Not()


    def getMatchOp(self, context, fieldType, valueType, operator):
        if operator in [ContOp.HAS, ContOp.NOT_HAS]:
            return MatchOp.HAS
        elif operator in [ContOp.IN, ContOp.NOT_IN]:
            return MatchOp.IN
        else:
            raise SyntaxError("Unsupported operator: " + str(operator))


