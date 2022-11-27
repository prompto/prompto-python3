from prompto.declaration.IDeclaration import IDeclaration

class IMethodDeclaration ( IDeclaration ):

	def asReference(self):
		from prompto.declaration.MethodDeclarationReference import MethodDeclarationReference
		return MethodDeclarationReference(self)