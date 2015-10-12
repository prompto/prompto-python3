from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestOperators(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAddAmount(self):
        self.compareResourceESE("operators/addAmount.pec")

    def testDivAmount(self):
        self.compareResourceESE("operators/divAmount.pec")

    def testIdivAmount(self):
        self.compareResourceESE("operators/idivAmount.pec")

    def testModAmount(self):
        self.compareResourceESE("operators/modAmount.pec")

    def testMultAmount(self):
        self.compareResourceESE("operators/multAmount.pec")

    def testSubAmount(self):
        self.compareResourceESE("operators/subAmount.pec")


