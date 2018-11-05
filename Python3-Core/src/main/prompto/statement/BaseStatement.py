from prompto.grammar.IDialectElement import IDialectElement
from prompto.parser.Section import Section


class BaseStatement ( Section, IDialectElement ):

    def canReturn(self):
        return False

    def isSimple(self):
        return False
