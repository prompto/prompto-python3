from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestOperators(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAddAmount(self):
        self.checkOutput("operators/addAmount.pec")

    def testDivAmount(self):
        self.checkOutput("operators/divAmount.pec")

    def testIdivAmount(self):
        self.checkOutput("operators/idivAmount.pec")

    def testModAmount(self):
        self.checkOutput("operators/modAmount.pec")

    def testMultAmount(self):
        self.checkOutput("operators/multAmount.pec")

    def testSubAmount(self):
        self.checkOutput("operators/subAmount.pec")


