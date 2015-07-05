from prompto.python.PythonSelectorExpression import PythonSelectorExpression

class PythonItemExpression ( PythonSelectorExpression ):

	def __init__(self, item):
		self.item = item
	
	def __str__(self):
		return str(self.parent) + "[" + str(self.item) + "]"

