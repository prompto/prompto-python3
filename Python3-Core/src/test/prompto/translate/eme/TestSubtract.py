from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSubtract(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSubDate(self):
        self.compareResourceEME("subtract/subDate.pec")

    def testSubDateTime(self):
        self.compareResourceEME("subtract/subDateTime.pec")

    def testSubDecimal(self):
        self.compareResourceEME("subtract/subDecimal.pec")

    def testSubDecimalEnum(self):
        self.compareResourceEME("subtract/subDecimalEnum.pec")

    def testSubInteger(self):
        self.compareResourceEME("subtract/subInteger.pec")

    def testSubIntegerEnum(self):
        self.compareResourceEME("subtract/subIntegerEnum.pec")

    def testSubList(self):
        self.compareResourceEME("subtract/subList.pec")

    def testSubPeriod(self):
        self.compareResourceEME("subtract/subPeriod.pec")

    def testSubSet(self):
        self.compareResourceEME("subtract/subSet.pec")

    def testSubTime(self):
        self.compareResourceEME("subtract/subTime.pec")


