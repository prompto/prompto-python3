from prompto.grammar.INamedValue import INamedValue
from prompto.parser.Section import Section


class Symbol ( Section , INamedValue):

    def __init__(self, symbol):
        super(Symbol, self).__init__()
        self.symbol = symbol

    def getSymbol(self):
        return self.symbol

    def getName(self):
        return self.symbol

    def register(self, context):
        context.registerValue(self)
