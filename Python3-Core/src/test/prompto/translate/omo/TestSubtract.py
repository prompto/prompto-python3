from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestSubtract(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSubDate(self):
        self.compareResourceOMO("subtract/subDate.poc")

    def testSubDateTime(self):
        self.compareResourceOMO("subtract/subDateTime.poc")

    def testSubDecimal(self):
        self.compareResourceOMO("subtract/subDecimal.poc")

    def testSubInteger(self):
        self.compareResourceOMO("subtract/subInteger.poc")

    def testSubList(self):
        self.compareResourceOMO("subtract/subList.poc")

    def testSubPeriod(self):
        self.compareResourceOMO("subtract/subPeriod.poc")

    def testSubSet(self):
        self.compareResourceOMO("subtract/subSet.poc")

    def testSubTime(self):
        self.compareResourceOMO("subtract/subTime.poc")


