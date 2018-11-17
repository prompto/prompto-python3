from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSubtract(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSubDate(self):
        self.compareResourceEOE("subtract/subDate.pec")

    def testSubDateTime(self):
        self.compareResourceEOE("subtract/subDateTime.pec")

    def testSubDecimal(self):
        self.compareResourceEOE("subtract/subDecimal.pec")

    def testSubDecimalEnum(self):
        self.compareResourceEOE("subtract/subDecimalEnum.pec")

    def testSubInteger(self):
        self.compareResourceEOE("subtract/subInteger.pec")

    def testSubIntegerEnum(self):
        self.compareResourceEOE("subtract/subIntegerEnum.pec")

    def testSubList(self):
        self.compareResourceEOE("subtract/subList.pec")

    def testSubPeriod(self):
        self.compareResourceEOE("subtract/subPeriod.pec")

    def testSubSet(self):
        self.compareResourceEOE("subtract/subSet.pec")

    def testSubTime(self):
        self.compareResourceEOE("subtract/subTime.pec")


