class SymbolList (list):

	def __init__(self, symbol = None):
		super(SymbolList, self).__init__()
		if symbol is not None:
			self.append(symbol)
