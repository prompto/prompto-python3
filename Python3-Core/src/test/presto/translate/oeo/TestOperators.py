from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestOperators(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAddAmount(self):
        self.compareResourceOEO("operators/addAmount.o")

    def testDivAmount(self):
        self.compareResourceOEO("operators/divAmount.o")

    def testIdivAmount(self):
        self.compareResourceOEO("operators/idivAmount.o")

    def testModAmount(self):
        self.compareResourceOEO("operators/modAmount.o")

    def testMultAmount(self):
        self.compareResourceOEO("operators/multAmount.o")

    def testSubAmount(self):
        self.compareResourceOEO("operators/subAmount.o")


