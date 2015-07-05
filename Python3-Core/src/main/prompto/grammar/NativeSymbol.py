from prompto.expression.IExpression import *
from prompto.grammar.Symbol import *


class NativeSymbol ( Symbol, IExpression ):

    def __init__(self, symbol, expression):
        super(NativeSymbol, self).__init__(symbol)
        self.expression = expression
        self.type_ = None

    def getExpression(self):
        return self.expression

    def getType(self, context):
        return self.type_

    def setType(self, type_):
        self.type_ = type_

    def __str__(self):
        return self.symbol + " with " + str(self.expression) + " as value"

    def toSDialect(self, writer):
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
        if not actual.isAssignableTo(context, self.type_.getDerivedFrom()):
            raise SyntaxError("Cannot assign " + actual.getName() + " to " + self.type_.getDerivedFrom().getName())
        return self.type_

    def interpret(self, context):
        return self.expression.interpret(context)
