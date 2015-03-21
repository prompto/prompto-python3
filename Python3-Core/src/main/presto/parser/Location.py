class Location(object):

    def __init__(self, token, isEnd=False):
        if token is None:
            pass
        self.index = token.tokenIndex
        self.line = token.line
        self.column = token.column
        if isEnd and token.text is not None:
            self.index += len(token.text)
            self.column += len(token.text)

    def getIndex(self):
        return self.index

    def getLine(self):
        return self.line

    def getColumn(self):
        return self.column
