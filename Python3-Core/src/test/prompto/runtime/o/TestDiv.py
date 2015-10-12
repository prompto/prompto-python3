from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestDiv(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDivDecimal(self):
        self.checkOutput("div/divDecimal.poc")

    def testDivInteger(self):
        self.checkOutput("div/divInteger.poc")

    def testIdivInteger(self):
        self.checkOutput("div/idivInteger.poc")

    def testModInteger(self):
        self.checkOutput("div/modInteger.poc")


