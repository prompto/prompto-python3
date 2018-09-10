import codecs
from antlr4 import *
from antlr4.InputStream import InputStream
from prompto.parser.EParser import EParser
from prompto.parser.EIndentingLexer import EIndentingLexer
from prompto.parser.EPromptoBuilder import EPromptoBuilder


class ECleverParser(EParser):

    def __init__(self, path=None, stream=None, text=None):
        self.path = path
        chars = None
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
        return self.doParse(self.declaration_list, True)

    def equalToken(self):
        return EParser.EQ

    def parse_standalone_type(self):
        return self.doParse(self.category_or_any_type, False)

    def doParse(self, rule, addLF):
        self.getTokenStream().tokenSource.addLF = addLF
        tree = rule()
        builder = EPromptoBuilder(self)
        walker = ParseTreeWalker()
        walker.walk(builder, tree)
        return builder.getNodeValue(tree)

