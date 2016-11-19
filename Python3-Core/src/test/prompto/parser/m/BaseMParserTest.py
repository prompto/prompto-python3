from prompto.utils.BaseParserTest import BaseParserTest


class BaseMParserTest(BaseParserTest):

    def __init__(self, args=None):
        super().__init__(args)

    def parseString(self, code):
        return self.parseMString(code)

    def parseResource(self, resourceName):
        return self.parseMResource(resourceName)

