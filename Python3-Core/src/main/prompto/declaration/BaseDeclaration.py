from prompto.parser.Section import Section
from prompto.declaration.IDeclaration import IDeclaration

class BaseDeclaration ( Section, IDeclaration ):

	def __init__(self, name):
		super().__init__()
		self.name = name
		
	def getName(self):
		return self.name
