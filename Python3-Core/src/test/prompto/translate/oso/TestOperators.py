from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestOperators(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAddAmount(self):
        self.compareResourceOSO("operators/addAmount.poc")

    def testDivAmount(self):
        self.compareResourceOSO("operators/divAmount.poc")

    def testIdivAmount(self):
        self.compareResourceOSO("operators/idivAmount.poc")

    def testModAmount(self):
        self.compareResourceOSO("operators/modAmount.poc")

    def testMultAmount(self):
        self.compareResourceOSO("operators/multAmount.poc")

    def testSubAmount(self):
        self.compareResourceOSO("operators/subAmount.poc")


