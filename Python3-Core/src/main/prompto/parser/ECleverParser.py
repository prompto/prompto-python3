import codecs
from antlr4 import *
from antlr4.InputStream import InputStream
from prompto.parser.EParser import EParser
from prompto.parser.EIndentingLexer import EIndentingLexer
from prompto.parser.EPromptoBuilder import EPromptoBuilder


class ECleverParser(EParser):

    def __init__(self, path=None, stream=None, text=None):
        self.path = path
        if stream is not None:
            bytes = stream.read()
            data = codecs.decode(bytes)
            chars = InputStream(data)
            stream.close()
        elif text is not None:
            chars = InputStream(text)
        if chars is not None:
            lexer = EIndentingLexer(chars)
            tokens = CommonTokenStream(lexer)
            super().__init__(tokens)


    def parse(self):
        tree = self.declaration_list()
        builder = EPromptoBuilder(self)
        walker = ParseTreeWalker()
        walker.walk(builder, tree)
        return builder.getNodeValue(tree)

    def equalToken(self):
        return EParser.EQ
