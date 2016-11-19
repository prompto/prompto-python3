from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestOperators(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAddAmount(self):
        self.compareResourceOMO("operators/addAmount.poc")

    def testDivAmount(self):
        self.compareResourceOMO("operators/divAmount.poc")

    def testIdivAmount(self):
        self.compareResourceOMO("operators/idivAmount.poc")

    def testModAmount(self):
        self.compareResourceOMO("operators/modAmount.poc")

    def testMultAmount(self):
        self.compareResourceOMO("operators/multAmount.poc")

    def testSubAmount(self):
        self.compareResourceOMO("operators/subAmount.poc")


