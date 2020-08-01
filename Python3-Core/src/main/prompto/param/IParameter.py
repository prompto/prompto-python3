from prompto.grammar.IDialectElement import IDialectElement
from prompto.grammar.INamedInstance import INamedInstance


class IParameter (INamedInstance, IDialectElement):

	def getType(self, context):
		raise Exception("Should never get there!")
