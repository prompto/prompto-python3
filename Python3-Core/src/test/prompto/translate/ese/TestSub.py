from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSub(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSubDate(self):
        self.compareResourceESE("sub/subDate.pec")

    def testSubDateTime(self):
        self.compareResourceESE("sub/subDateTime.pec")

    def testSubDecimal(self):
        self.compareResourceESE("sub/subDecimal.pec")

    def testSubDecimalEnum(self):
        self.compareResourceESE("sub/subDecimalEnum.pec")

    def testSubInteger(self):
        self.compareResourceESE("sub/subInteger.pec")

    def testSubIntegerEnum(self):
        self.compareResourceESE("sub/subIntegerEnum.pec")

    def testSubPeriod(self):
        self.compareResourceESE("sub/subPeriod.pec")

    def testSubTime(self):
        self.compareResourceESE("sub/subTime.pec")


