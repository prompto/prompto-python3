from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestOperators(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAddAmount(self):
        self.compareResourceEPE("operators/addAmount.e")

    def testDivAmount(self):
        self.compareResourceEPE("operators/divAmount.e")

    def testIdivAmount(self):
        self.compareResourceEPE("operators/idivAmount.e")

    def testModAmount(self):
        self.compareResourceEPE("operators/modAmount.e")

    def testMultAmount(self):
        self.compareResourceEPE("operators/multAmount.e")

    def testSubAmount(self):
        self.compareResourceEPE("operators/subAmount.e")


