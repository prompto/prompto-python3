from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestSubtract(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSubDate(self):
        self.compareResourceOEO("subtract/subDate.poc")

    def testSubDateTime(self):
        self.compareResourceOEO("subtract/subDateTime.poc")

    def testSubDecimal(self):
        self.compareResourceOEO("subtract/subDecimal.poc")

    def testSubInteger(self):
        self.compareResourceOEO("subtract/subInteger.poc")

    def testSubList(self):
        self.compareResourceOEO("subtract/subList.poc")

    def testSubPeriod(self):
        self.compareResourceOEO("subtract/subPeriod.poc")

    def testSubSet(self):
        self.compareResourceOEO("subtract/subSet.poc")

    def testSubTime(self):
        self.compareResourceOEO("subtract/subTime.poc")


