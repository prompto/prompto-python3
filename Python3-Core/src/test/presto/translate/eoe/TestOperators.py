from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestOperators(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAddAmount(self):
        self.compareResourceEOE("operators/addAmount.e")

    def testDivAmount(self):
        self.compareResourceEOE("operators/divAmount.e")

    def testIdivAmount(self):
        self.compareResourceEOE("operators/idivAmount.e")

    def testModAmount(self):
        self.compareResourceEOE("operators/modAmount.e")

    def testMultAmount(self):
        self.compareResourceEOE("operators/multAmount.e")

    def testSubAmount(self):
        self.compareResourceEOE("operators/subAmount.e")


