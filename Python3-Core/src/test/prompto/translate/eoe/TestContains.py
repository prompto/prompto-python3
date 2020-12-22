from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestContains(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testHasAllDict(self):
        self.compareResourceEOE("contains/hasAllDict.pec")

    def testHasAllList(self):
        self.compareResourceEOE("contains/hasAllList.pec")

    def testHasAllRange(self):
        self.compareResourceEOE("contains/hasAllRange.pec")

    def testHasAllSet(self):
        self.compareResourceEOE("contains/hasAllSet.pec")

    def testHasAllText(self):
        self.compareResourceEOE("contains/hasAllText.pec")

    def testHasAllTuple(self):
        self.compareResourceEOE("contains/hasAllTuple.pec")

    def testHasAnyDict(self):
        self.compareResourceEOE("contains/hasAnyDict.pec")

    def testHasAnyList(self):
        self.compareResourceEOE("contains/hasAnyList.pec")

    def testHasAnyRange(self):
        self.compareResourceEOE("contains/hasAnyRange.pec")

    def testHasAnySet(self):
        self.compareResourceEOE("contains/hasAnySet.pec")

    def testHasAnyText(self):
        self.compareResourceEOE("contains/hasAnyText.pec")

    def testHasAnyTuple(self):
        self.compareResourceEOE("contains/hasAnyTuple.pec")

    def testInCharacterRange(self):
        self.compareResourceEOE("contains/inCharacterRange.pec")

    def testInDateRange(self):
        self.compareResourceEOE("contains/inDateRange.pec")

    def testInDict(self):
        self.compareResourceEOE("contains/inDict.pec")

    def testInIntegerRange(self):
        self.compareResourceEOE("contains/inIntegerRange.pec")

    def testInList(self):
        self.compareResourceEOE("contains/inList.pec")

    def testInSet(self):
        self.compareResourceEOE("contains/inSet.pec")

    def testInText(self):
        self.compareResourceEOE("contains/inText.pec")

    def testInTextEnum(self):
        self.compareResourceEOE("contains/inTextEnum.pec")

    def testInTimeRange(self):
        self.compareResourceEOE("contains/inTimeRange.pec")

    def testInTuple(self):
        self.compareResourceEOE("contains/inTuple.pec")

    def testNinCharacterRange(self):
        self.compareResourceEOE("contains/ninCharacterRange.pec")

    def testNinDateRange(self):
        self.compareResourceEOE("contains/ninDateRange.pec")

    def testNinDict(self):
        self.compareResourceEOE("contains/ninDict.pec")

    def testNinIntegerRange(self):
        self.compareResourceEOE("contains/ninIntegerRange.pec")

    def testNinList(self):
        self.compareResourceEOE("contains/ninList.pec")

    def testNinSet(self):
        self.compareResourceEOE("contains/ninSet.pec")

    def testNinText(self):
        self.compareResourceEOE("contains/ninText.pec")

    def testNinTimeRange(self):
        self.compareResourceEOE("contains/ninTimeRange.pec")


