from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestOperators(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAddAmount(self):
        self.compareResourceOEO("operators/addAmount.poc")

    def testDivAmount(self):
        self.compareResourceOEO("operators/divAmount.poc")

    def testIdivAmount(self):
        self.compareResourceOEO("operators/idivAmount.poc")

    def testModAmount(self):
        self.compareResourceOEO("operators/modAmount.poc")

    def testMultAmount(self):
        self.compareResourceOEO("operators/multAmount.poc")

    def testSubAmount(self):
        self.compareResourceOEO("operators/subAmount.poc")


