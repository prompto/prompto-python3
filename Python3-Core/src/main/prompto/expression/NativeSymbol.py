from prompto.expression.IExpression import *
from prompto.expression.Symbol import *
from prompto.error.SyntaxError import SyntaxError
from prompto.value.Text import Text


class NativeSymbol ( Symbol, IExpression ):

    def __init__(self, symbol, expression):
        super(NativeSymbol, self).__init__(symbol)
        self.expression = expression
        self.itype = None

    def getExpression(self):
        return self.expression

    def getType(self, context):
        return self.itype

    def setType(self, itype):
        self.itype = itype

    def __str__(self):
        return self.symbol

    def toMDialect(self, writer):
        writer.append(self.symbol)
        writer.append(" = ")
        self.expression.toDialect(writer)

    def toODialect(self, writer):
        writer.append(self.symbol)
        writer.append(" = ")
        self.expression.toDialect(writer)

    def toEDialect(self, writer):
        writer.append(self.symbol)
        writer.append(" with ")
        self.expression.toDialect(writer)
        writer.append(" as value")


    def __eq__(self, obj):
        if id(obj)==id(self):
            return True
        if obj is None:
            return False
        if not isinstance(obj, NativeSymbol):
            return False
        return self.getName()==obj.getName() \
                and self.getExpression()==obj.getExpression()

    def check(self, context):
        actual = self.expression.check(context)
        if not self.itype.getDerivedFrom().isAssignableFrom(context, actual):
            raise SyntaxError("Cannot assign " + actual.getName() + " to " + self.itype.getDerivedFrom().getName())
        return self.itype

    def interpret(self, context):
        return self


    def getMemberValue(self, context, name, autoCreate):
        if "name" == name:
            return Text(self.getName())
        elif "value" == name:
            return self.expression.interpret(context)
        else:
            return super().getMemberValue(context, name, autoCreate)