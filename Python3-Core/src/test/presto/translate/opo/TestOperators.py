from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestOperators(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAddAmount(self):
        self.compareResourceOPO("operators/addAmount.o")

    def testDivAmount(self):
        self.compareResourceOPO("operators/divAmount.o")

    def testIdivAmount(self):
        self.compareResourceOPO("operators/idivAmount.o")

    def testModAmount(self):
        self.compareResourceOPO("operators/modAmount.o")

    def testMultAmount(self):
        self.compareResourceOPO("operators/multAmount.o")

    def testSubAmount(self):
        self.compareResourceOPO("operators/subAmount.o")


