from presto.declaration.BaseDeclaration import BaseDeclaration


class BaseCategoryMethodDeclaration ( BaseDeclaration ):

	def __init__(self, name, arguments, instructions):
		super(BaseCategoryMethodDeclaration, self).__init__(name)
		self.arguments = arguments
		self.instructions = instructions
	
	def getArguments(self):
		return self.arguments

	def interpret(self, context):
		return self.instructions.interpret(context)
