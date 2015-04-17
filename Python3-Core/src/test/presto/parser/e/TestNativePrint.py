from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out


class TestIssues(BaseEParserTest):

    def setUp(self):
        super(type(self), self).setUp()
        Out.init()

    def tearDown(self):
        Out.restore()

    def testNativePrint(self):
        self.runResource("native/print.pec")
        self.assertEquals("name=IBM", Out.read())
