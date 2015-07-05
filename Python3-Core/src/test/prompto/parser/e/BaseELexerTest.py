from antlr4 import Token
from antlr4.InputStream import InputStream
from prompto.parser.ELexer import ELexer
from prompto.parser.EIndentingLexer import EIndentingLexer

class BaseELexerTest(object):

    def parseTokens(self, lexer):
        result = []
        t = lexer.nextToken()
        while t.type!=Token.EOF:
            if t.channel!=ELexer.HIDDEN:
                result.append(t)
            t = lexer.nextToken()
        return result

    def parseTokenTypes(self, lexer):
        tokens = self.parseTokens(lexer)
        result = []
        for t in tokens:
            result.append(t.getType())
        return result

    def parseTokenNames(self, lexer):
        tokens = self.parseTokens(lexer)
        s = ""
        for t in tokens:
            s += lexer.getTokenName(t) + " "
        return s[0:len(s)-1]

    def newTokenStreamFromString(self, input_):
        stream = InputStream(input_)
        return EIndentingLexer(stream)

    def parseTokenNamesFromString(self, input_):
        lexer = self.newTokenStreamFromString(input_)
        return self.parseTokenNames(lexer)

    def tokenNamesAsString(self, tokenTypes):
        lexer = EIndentingLexer(None)
        s = ""
        for t in tokenTypes:
            s += lexer.getTokenName(type_=t) + " "
        return s[0:len(s)-1]
