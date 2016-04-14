from prompto.utils.BaseParserTest import BaseParserTest


class BaseSParserTest(BaseParserTest):

    def __init__(self, args=None):
        super().__init__(args)

    def parseString(self, code):
        return self.parseSString(code)

    def parseResource(self, resourceName):
        return self.parseSResource(resourceName)

