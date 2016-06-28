from prompto.utils.ObjectList import ObjectList



class SymbolList (ObjectList):

    def __init__(self, symbol = None):
        super(SymbolList, self).__init__()
        if symbol is not None:
            self.append(symbol)



    def __str__(self):
        return "[" + super(SymbolList, self).__str__() + "]"