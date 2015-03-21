from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestDiv(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDivDecimal(self):
        self.checkOutput("div/divDecimal.o")

    def testDivInteger(self):
        self.checkOutput("div/divInteger.o")

    def testIdivInteger(self):
        self.checkOutput("div/idivInteger.o")

    def testModInteger(self):
        self.checkOutput("div/modInteger.o")


