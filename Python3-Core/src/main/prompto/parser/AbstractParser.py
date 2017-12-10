from antlr4 import Parser, Token

class AbstractParser(Parser):

    def __init__(self, input_, output_):
        super().__init__(input_, output_)
        self.path = ""

    def isText(self, token:Token, text:str):
        return text==token.text

    def was(self, type:int):
        return self.lastHiddenTokenType()==type

    def wasNot(self, type:int):
        return self.lastHiddenTokenType()!=type

    def willBe(self, type:int):
        return self._input.LA(1)==type

    def willNotBe(self, type:int):
        return self._input.LA(1)!=type

    def nextHiddenTokenType(self):
        hidden = self._input.getHiddenTokensToRight(self._input.index-1)
        if hidden is None or len(hidden)==0:
            return 0
        else:
            return hidden[0].type

    def willBeAOrAn(self):
        return self.willBeText("a") or self.willBeText("an")

    def willBeText(self, text):
        return text==self._input.LT(1).text


    def lastHiddenTokenType(self):
        hidden = self._input.getHiddenTokensToLeft(self._input.index)
        if hidden is None or len(hidden)==0:
            return 0
        else:
            return hidden[-1].type

