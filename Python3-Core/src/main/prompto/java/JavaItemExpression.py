from prompto.java.JavaSelectorExpression import JavaSelectorExpression

class JavaItemExpression ( JavaSelectorExpression ):

	def __init__(self, item):
		self.item = item
	
	def __str__(self):
		return str(self.parent) + "[" + str(self.item) + "]"
