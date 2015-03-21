import codecs
from antlr4 import *
from antlr4.InputStream import InputStream
from presto.parser.PParser import PParser
from presto.parser.PIndentingLexer import PIndentingLexer
from presto.parser.PPrestoBuilder import PPrestoBuilder


class PCleverParser(PParser):

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
            lexer = PIndentingLexer(chars)
            tokens = CommonTokenStream(lexer)
            super().__init__(tokens)


    def parse(self):
        tree = self.declaration_list()
        builder = PPrestoBuilder(self)
        walker = ParseTreeWalker()
        walker.walk(builder, tree)
        return builder.getNodeValue(tree)

    def equalToken(self):
        return PParser.EQ
