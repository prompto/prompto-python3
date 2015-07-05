from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out


class TestIssues(BaseEParserTest):

    def setUp(self):
        super(type(self), self).setUp()
        Out.init()

    def tearDown(self):
        Out.restore()

    def testMinimal(self):
        self.runResourceMethod("issues/minimal.pec", "mainNoCmdLine", None)
        self.checkExpected("issues/minimal.pec")
