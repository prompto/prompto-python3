from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestSub(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSubDate(self):
        self.compareResourceOSO("sub/subDate.poc")

    def testSubDateTime(self):
        self.compareResourceOSO("sub/subDateTime.poc")

    def testSubDecimal(self):
        self.compareResourceOSO("sub/subDecimal.poc")

    def testSubInteger(self):
        self.compareResourceOSO("sub/subInteger.poc")

    def testSubPeriod(self):
        self.compareResourceOSO("sub/subPeriod.poc")

    def testSubTime(self):
        self.compareResourceOSO("sub/subTime.poc")


