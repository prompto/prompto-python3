from prompto.parser.OLexer import OLexer
from prompto.parser.Dialect import Dialect
from prompto.parser.Utils import extractTokenNames


class ONamingLexer(OLexer):

	tokenNames = extractTokenNames(OLexer)

	@classmethod
	def getTokenName(cls, token=None, itype=None):
		if itype is None:
			itype = token.getType()
		return cls.tokenNames[itype]

	def __init__(self, input_):
		super(ONamingLexer, self).__init__(input_)

	def getDialect(self):
		return Dialect.O
