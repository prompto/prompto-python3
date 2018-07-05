from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestWidget(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testMinimal(self):
        self.checkOutput("widget/minimal.poc")

    def testNative(self):
        self.checkOutput("widget/native.poc")


