from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestSub(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSubDate(self):
        self.compareResourceOMO("sub/subDate.poc")

    def testSubDateTime(self):
        self.compareResourceOMO("sub/subDateTime.poc")

    def testSubDecimal(self):
        self.compareResourceOMO("sub/subDecimal.poc")

    def testSubInteger(self):
        self.compareResourceOMO("sub/subInteger.poc")

    def testSubPeriod(self):
        self.compareResourceOMO("sub/subPeriod.poc")

    def testSubTime(self):
        self.compareResourceOMO("sub/subTime.poc")


