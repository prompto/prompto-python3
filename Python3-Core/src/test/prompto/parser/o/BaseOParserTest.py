from prompto.utils.BaseParserTest import BaseParserTest


class BaseOParserTest(BaseParserTest):

    def __init__(self, args=None):
        super().__init__(args)

    def parseString(self, code):
        return self.parseOString(code)

    def parseResource(self, resourceName):
        return self.parseOResource(resourceName)

