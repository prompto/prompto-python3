from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestOperators(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAddAmount(self):
        self.checkOutput("operators/addAmount.e")

    def testDivAmount(self):
        self.checkOutput("operators/divAmount.e")

    def testIdivAmount(self):
        self.checkOutput("operators/idivAmount.e")

    def testModAmount(self):
        self.checkOutput("operators/modAmount.e")

    def testMultAmount(self):
        self.checkOutput("operators/multAmount.e")

    def testSubAmount(self):
        self.checkOutput("operators/subAmount.e")


