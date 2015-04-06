from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestOperators(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAddAmount(self):
        self.compareResourceEOE("operators/addAmount.pec")

    def testDivAmount(self):
        self.compareResourceEOE("operators/divAmount.pec")

    def testIdivAmount(self):
        self.compareResourceEOE("operators/idivAmount.pec")

    def testModAmount(self):
        self.compareResourceEOE("operators/modAmount.pec")

    def testMultAmount(self):
        self.compareResourceEOE("operators/multAmount.pec")

    def testSubAmount(self):
        self.compareResourceEOE("operators/subAmount.pec")


