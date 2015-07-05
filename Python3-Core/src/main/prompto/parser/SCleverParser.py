import codecs
from antlr4 import *
from antlr4.InputStream import InputStream
from prompto.parser.SParser import SParser
from prompto.parser.SIndentingLexer import SIndentingLexer
from prompto.parser.SPromptoBuilder import SPromptoBuilder


class SCleverParser(SParser):

    def __init__(self, path=None, stream=None, text=None):
        chars = None
        self.path = path
        if stream is not None:
            bytes = stream.read()
            data = codecs.decode(bytes)
            chars = InputStream(data)
            stream.close()
        elif text is not None:
            chars = InputStream(text)
        if chars is not None:
            lexer = SIndentingLexer(chars)
            tokens = CommonTokenStream(lexer)
            super().__init__(tokens)


    def parse(self):
        tree = self.declaration_list()
        builder = SPromptoBuilder(self)
        walker = ParseTreeWalker()
        walker.walk(builder, tree)
        return builder.getNodeValue(tree)

    def equalToken(self):
        return SParser.EQ
