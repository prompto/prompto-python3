from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestSub(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSubDate(self):
        self.compareResourceOEO("sub/subDate.o")

    def testSubDateTime(self):
        self.compareResourceOEO("sub/subDateTime.o")

    def testSubDecimal(self):
        self.compareResourceOEO("sub/subDecimal.o")

    def testSubInteger(self):
        self.compareResourceOEO("sub/subInteger.o")

    def testSubPeriod(self):
        self.compareResourceOEO("sub/subPeriod.o")

    def testSubTime(self):
        self.compareResourceOEO("sub/subTime.o")


