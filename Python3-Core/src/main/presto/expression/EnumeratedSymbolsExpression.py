from presto.declaration.IDeclaration import IDeclaration
from presto.declaration.IEnumeratedDeclaration import IEnumeratedDeclaration
from presto.expression.IExpression import IExpression
from presto.type.ListType import ListType


class EnumeratedSymbolsExpression ( IExpression ):

	def __init__(self, name):
		super(EnumeratedSymbolsExpression, self).__init__()
		self.name = name

	def __str__(self):
		return self.name

	def check(self, context):
		named = context.getRegisteredDeclaration(IDeclaration, self.name)
		if not isinstance(named, IEnumeratedDeclaration):
			raise SyntaxError(self.name + " is not an enumerated type!")
		return ListType(named.getType(context))

	def interpret(self, context):
		named = context.getRegisteredDeclaration(IDeclaration, self.name)
		if not isinstance(named, IEnumeratedDeclaration):
			raise SyntaxError(self.name + " is not an enumerated type!")
		return named.getSymbols()
