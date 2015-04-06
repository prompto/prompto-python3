from antlr4 import *
from antlr4.Token import CommonToken
from presto.parser.SLexer import SLexer
from presto.parser.Dialect import Dialect

class SIndentingLexer(SLexer):

    @classmethod
    def getTokenName(cls, token=None, type_=None):
        if type_ is None:
            type_ = token.type
        return cls.symbolicNames[type_]

    def __init__(self, input_):
        super().__init__(input_)
        self.tokens = []
        self.indents = [0]
        self.wasLF = False
        self.addLF = True

    def getDialect(self):
        return Dialect.S

    def nextToken(self):
        t = self.getNextToken()
        self.wasLF = t.type==SLexer.LF
        return t

    def getNextToken(self):
        if len(self.tokens)>0:
            return self.tokens.pop(0)
        self.interpret(super().nextToken())
        return self.nextToken()

    def interpret(self, token:CommonToken):
        t = token.type
        if t==Token.EOF:
            self.interpretEOF(token)
        elif t==SLexer.LF_TAB:
            self.interpretLFTAB(token)
        else:
            self.interpretAnyToken(token)

    def interpretEOF(self, eof):
        # gracefully handle missing lf/dedents
        while len(self.indents)>1:
            self.tokens.append(self.deriveToken(eof, SLexer.DEDENT))
            self.tokens.append(self.deriveToken(eof, SLexer.LF))
            self.wasLF = True
            self.indents.pop()
        # gracefully handle missing lf
        if self.addLF and not self.wasLF:
            self.tokens.append(self.deriveToken(eof, SLexer.LF))
        self.tokens.append(eof)

    def interpretLFTAB(self, lftab:CommonToken):
        # count TABs following LF
        indentCount = self.countIndents(lftab.text)
        next = super().nextToken()
        # if this was an empty line, simply skip it
        if next.type==Token.EOF or next.type==SLexer.LF_TAB:
            self.tokens.append(self.deriveToken(lftab, SLexer.LF))
            self.interpret(next)
        elif indentCount==self.indents[-1]:
            self.tokens.append(self.deriveToken(lftab, SLexer.LF))
            self.interpret(next)
        elif indentCount > self.indents[-1]:
            self.tokens.append(self.deriveToken(lftab, SLexer.LF))
            self.tokens.append(self.deriveToken(lftab, SLexer.INDENT))
            self.indents.append(indentCount)
            self.interpret(next)
        else:
            while len(self.indents)>1 and indentCount<self.indents[-1]:
                self.tokens.append(self.deriveToken(lftab, SLexer.DEDENT))
                self.tokens.append(self.deriveToken(lftab, SLexer.LF))
                self.indents.pop()
            if indentCount > self.indents[-1]:
                pass # TODO, fire an error through token
            self.interpret(next)

    def deriveToken(self, token:CommonToken, type:int):
        res = token.clone()
        res.type = type
        return res

    def countIndents(self, text:str):
        count = 0
        for c in text:
            if c==' ':
                count += 1
            elif c=='\t':
                count += 4
        return int(count/4)

    def interpretAnyToken(self, token):
        self.tokens.append(token)
