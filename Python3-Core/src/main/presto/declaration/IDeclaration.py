from presto.grammar.IDialectElement import IDialectElement
from presto.grammar.INamed import INamed
from presto.parser.ISection import ISection

class IDeclaration (INamed, ISection, IDialectElement):
	
	pass