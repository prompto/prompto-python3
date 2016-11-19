from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSub(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSubDate(self):
        self.compareResourceEME("sub/subDate.pec")

    def testSubDateTime(self):
        self.compareResourceEME("sub/subDateTime.pec")

    def testSubDecimal(self):
        self.compareResourceEME("sub/subDecimal.pec")

    def testSubDecimalEnum(self):
        self.compareResourceEME("sub/subDecimalEnum.pec")

    def testSubInteger(self):
        self.compareResourceEME("sub/subInteger.pec")

    def testSubIntegerEnum(self):
        self.compareResourceEME("sub/subIntegerEnum.pec")

    def testSubPeriod(self):
        self.compareResourceEME("sub/subPeriod.pec")

    def testSubTime(self):
        self.compareResourceEME("sub/subTime.pec")


