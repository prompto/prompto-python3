from presto.grammar.INamedValue import INamedValue
from presto.declaration.AttributeDeclaration import *


class Attribute ( INamedValue ):

	def __init__(self, name):
		super(Attribute, self).__init__()
		self.name = name

	def getName(self):
		return self.name

	def getType(self, context):
		declaration = context.getRegisteredDeclaration(AttributeDeclaration, self.name)
		return declaration.getType(context)
