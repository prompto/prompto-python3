from prompto.grammar.INamedValue import INamedValue
from prompto.runtime.Variable import Variable
from prompto.statement.SimpleStatement import SimpleStatement
from prompto.type.TupleType import TupleType
from prompto.type.VoidType import VoidType
from prompto.value.IntegerValue import IntegerValue
from prompto.value.TupleValue import TupleValue
from prompto.error.SyntaxError import SyntaxError

class AssignTupleStatement(SimpleStatement):

    def __init__(self, names):
        super().__init__()
        self.names = names
        self.expression = None

    def __str__(self):
        return str(self.names) + " = " + str(self.expression)

    def toDialect(self, writer):
        self.names.toDialect(writer, False)
        writer.append(" = ")
        self.expression.toDialect(writer)

    def append(self, name):
        self.names.append(name)

    def getNames(self):
        return self.names

    def setExpression(self, expression):
        self.expression = expression

    def getExpression(self):
        return self.expression

    def __eq__(self, obj):
        if id(obj) == id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, AssignTupleStatement):
            return False
        return self.getNames() == obj.getNames() and self.getExpression() == obj.getExpression()

    def check(self, context):
        itype = self.expression.check(context)
        if itype != TupleType.instance:
            raise SyntaxError("Expecting a tuple expression, got " + itype.getName())
        for name in self.names:
            actual = context.getRegistered(name)
            if actual is None:
                actualType = self.expression.check(context)
                context.registerValue(Variable(name, actualType))
            else:
                # need to check type compatibility
                actualType = actual.getType(context)
                newType = self.expression.check(context)
                actualType.checkAssignableFrom(context, newType)
        return VoidType.instance

    def interpret(self, context):
        value = self.expression.interpret(context)
        if not isinstance(value, TupleValue):
            raise SyntaxError("Expecting a tuple expression, got " + type(value).__name__)
        i = 1
        for name in self.names:
            item = value.getItem(context, IntegerValue(i))
            i += 1
            if context.getRegisteredValue(INamedValue, name) is None:
                context.registerValue(Variable(name, item.itype))
            context.setValue(name, item)
        return None
