from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out


class TestIssues(BaseEParserTest):

    def setUp(self):
        super(type(self), self).setUp()
        Out.init()

    def tearDown(self):
        Out.restore()

    def testMinimal(self):
        self.runResourceMethod("issues/minimal.e", "mainNoCmdLine", None)
        self.checkExpected("issues/minimal.e")
