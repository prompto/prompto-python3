from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestContains(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testHasAllDict(self):
        self.compareResourceEME("contains/hasAllDict.pec")

    def testHasAllList(self):
        self.compareResourceEME("contains/hasAllList.pec")

    def testHasAllRange(self):
        self.compareResourceEME("contains/hasAllRange.pec")

    def testHasAllSet(self):
        self.compareResourceEME("contains/hasAllSet.pec")

    def testHasAllText(self):
        self.compareResourceEME("contains/hasAllText.pec")

    def testHasAllTuple(self):
        self.compareResourceEME("contains/hasAllTuple.pec")

    def testHasAnyDict(self):
        self.compareResourceEME("contains/hasAnyDict.pec")

    def testHasAnyList(self):
        self.compareResourceEME("contains/hasAnyList.pec")

    def testHasAnyRange(self):
        self.compareResourceEME("contains/hasAnyRange.pec")

    def testHasAnySet(self):
        self.compareResourceEME("contains/hasAnySet.pec")

    def testHasAnyText(self):
        self.compareResourceEME("contains/hasAnyText.pec")

    def testHasAnyTuple(self):
        self.compareResourceEME("contains/hasAnyTuple.pec")

    def testInCharacterRange(self):
        self.compareResourceEME("contains/inCharacterRange.pec")

    def testInDateRange(self):
        self.compareResourceEME("contains/inDateRange.pec")

    def testInDict(self):
        self.compareResourceEME("contains/inDict.pec")

    def testInIntegerRange(self):
        self.compareResourceEME("contains/inIntegerRange.pec")

    def testInList(self):
        self.compareResourceEME("contains/inList.pec")

    def testInSet(self):
        self.compareResourceEME("contains/inSet.pec")

    def testInText(self):
        self.compareResourceEME("contains/inText.pec")

    def testInTextEnum(self):
        self.compareResourceEME("contains/inTextEnum.pec")

    def testInTimeRange(self):
        self.compareResourceEME("contains/inTimeRange.pec")

    def testInTuple(self):
        self.compareResourceEME("contains/inTuple.pec")

    def testNinCharacterRange(self):
        self.compareResourceEME("contains/ninCharacterRange.pec")

    def testNinDateRange(self):
        self.compareResourceEME("contains/ninDateRange.pec")

    def testNinDict(self):
        self.compareResourceEME("contains/ninDict.pec")

    def testNinIntegerRange(self):
        self.compareResourceEME("contains/ninIntegerRange.pec")

    def testNinList(self):
        self.compareResourceEME("contains/ninList.pec")

    def testNinSet(self):
        self.compareResourceEME("contains/ninSet.pec")

    def testNinText(self):
        self.compareResourceEME("contains/ninText.pec")

    def testNinTimeRange(self):
        self.compareResourceEME("contains/ninTimeRange.pec")


