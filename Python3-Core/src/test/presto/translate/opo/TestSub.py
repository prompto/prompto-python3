from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestSub(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSubDate(self):
        self.compareResourceOPO("sub/subDate.o")

    def testSubDateTime(self):
        self.compareResourceOPO("sub/subDateTime.o")

    def testSubDecimal(self):
        self.compareResourceOPO("sub/subDecimal.o")

    def testSubInteger(self):
        self.compareResourceOPO("sub/subInteger.o")

    def testSubPeriod(self):
        self.compareResourceOPO("sub/subPeriod.o")

    def testSubTime(self):
        self.compareResourceOPO("sub/subTime.o")


