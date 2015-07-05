from prompto.expression.IExpression import IExpression
from prompto.grammar.Symbol import Symbol


class SymbolExpression ( IExpression ):

    def __init__(self, name):
        super(SymbolExpression, self).__init__()
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

    def toDialect(self, writer):
        writer.append(self.name)

    def check(self, context):
        symbol = context.getRegisteredValue(Symbol, self.name)
        if symbol is None:
            raise SyntaxError("Unknown symbol:" + self.name)
        return symbol.check(context)

    def interpret(self, context):
        symbol = context.getRegisteredValue(Symbol, self.name)
        if symbol is None:
            raise SyntaxError("Unknown symbol:" + self.name)
        return symbol.interpret(context)
