from prompto.utils.BaseParserTest import BaseParserTest
from prompto.parser.ECleverParser import *


class BaseEParserTest(BaseParserTest):

    def __init__(self, args=None):
        super().__init__(args)

    def parseString(self, code):
        return self.parseEString(code)

    def parseResource(self, resourceName):
        return self.parseEResource(resourceName)


