from prompto.grammar.IDialectElement import IDialectElement
from prompto.grammar.INamed import INamed
from prompto.parser.ISection import ISection


class IDeclaration (INamed, ISection, IDialectElement):

	def check(self, context):
		pass

