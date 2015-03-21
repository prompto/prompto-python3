from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestDiv(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDivDecimal(self):
        self.checkOutput("div/divDecimal.e")

    def testDivInteger(self):
        self.checkOutput("div/divInteger.e")

    def testIdivInteger(self):
        self.checkOutput("div/idivInteger.e")

    def testModInteger(self):
        self.checkOutput("div/modInteger.e")


