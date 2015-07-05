from prompto.csharp.CSharpSelectorExpression import CSharpSelectorExpression

class CSharpItemExpression ( CSharpSelectorExpression ):

	def __init__(self, item):
		self.item = item
	
	def __str__(self):
		return str(self.parent) + "[" + str(self.item) + "]"

