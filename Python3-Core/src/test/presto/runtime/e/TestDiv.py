from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestDiv(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDivDecimal(self):
        self.checkOutput("div/divDecimal.pec")

    def testDivInteger(self):
        self.checkOutput("div/divInteger.pec")

    def testIdivInteger(self):
        self.checkOutput("div/idivInteger.pec")

    def testModInteger(self):
        self.checkOutput("div/modInteger.pec")


