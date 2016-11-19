from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestOperators(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAddAmount(self):
        self.compareResourceEME("operators/addAmount.pec")

    def testDivAmount(self):
        self.compareResourceEME("operators/divAmount.pec")

    def testIdivAmount(self):
        self.compareResourceEME("operators/idivAmount.pec")

    def testModAmount(self):
        self.compareResourceEME("operators/modAmount.pec")

    def testMultAmount(self):
        self.compareResourceEME("operators/multAmount.pec")

    def testSubAmount(self):
        self.compareResourceEME("operators/subAmount.pec")


