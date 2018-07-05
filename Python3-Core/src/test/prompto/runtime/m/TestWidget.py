from prompto.parser.m.BaseMParserTest import BaseMParserTest
from prompto.runtime.utils.Out import Out

class TestWidget(BaseMParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testMinimal(self):
        self.checkOutput("widget/minimal.pmc")

    def testNative(self):
        self.checkOutput("widget/native.pmc")


