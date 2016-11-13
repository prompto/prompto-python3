from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSub(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSubDate(self):
        self.compareResourceEOE("sub/subDate.pec")

    def testSubDateTime(self):
        self.compareResourceEOE("sub/subDateTime.pec")

    def testSubDecimal(self):
        self.compareResourceEOE("sub/subDecimal.pec")

    def testSubDecimalEnum(self):
        self.compareResourceEOE("sub/subDecimalEnum.pec")

    def testSubInteger(self):
        self.compareResourceEOE("sub/subInteger.pec")

    def testSubIntegerEnum(self):
        self.compareResourceEOE("sub/subIntegerEnum.pec")

    def testSubPeriod(self):
        self.compareResourceEOE("sub/subPeriod.pec")

    def testSubTime(self):
        self.compareResourceEOE("sub/subTime.pec")


