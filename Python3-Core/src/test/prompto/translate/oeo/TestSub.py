from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestSub(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSubDate(self):
        self.compareResourceOEO("sub/subDate.poc")

    def testSubDateTime(self):
        self.compareResourceOEO("sub/subDateTime.poc")

    def testSubDecimal(self):
        self.compareResourceOEO("sub/subDecimal.poc")

    def testSubInteger(self):
        self.compareResourceOEO("sub/subInteger.poc")

    def testSubPeriod(self):
        self.compareResourceOEO("sub/subPeriod.poc")

    def testSubTime(self):
        self.compareResourceOEO("sub/subTime.poc")


