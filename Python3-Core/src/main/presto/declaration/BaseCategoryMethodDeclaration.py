from presto.declaration.BaseDeclaration import BaseDeclaration
from presto.declaration.ICategoryMethodDeclaration import ICategoryMethodDeclaration


class BaseCategoryMethodDeclaration ( BaseDeclaration, ICategoryMethodDeclaration ):

	def __init__(self, name, arguments, instructions):
		super(BaseCategoryMethodDeclaration, self).__init__(name)
		self.arguments = arguments;
		self.instructions = instructions;
	
	def getArguments(self):
		return self.arguments;

	def interpret(self, context):
		return self.instructions.interpret(context)
