from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestOperators(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAddAmount(self):
        self.checkOutput("operators/addAmount.o")

    def testDivAmount(self):
        self.checkOutput("operators/divAmount.o")

    def testIdivAmount(self):
        self.checkOutput("operators/idivAmount.o")

    def testModAmount(self):
        self.checkOutput("operators/modAmount.o")

    def testMultAmount(self):
        self.checkOutput("operators/multAmount.o")

    def testSubAmount(self):
        self.checkOutput("operators/subAmount.o")


