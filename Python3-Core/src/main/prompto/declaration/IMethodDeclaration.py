from prompto.declaration.IDeclaration import IDeclaration
from prompto.runtime.ContextFlags import ContextFlags


class IMethodDeclaration ( IDeclaration ):

	# noinspection PyMethodOverriding
	def check(self, context, flags:ContextFlags):
		pass