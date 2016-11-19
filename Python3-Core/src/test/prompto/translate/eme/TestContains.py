from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestContains(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testContainsAllDict(self):
        self.compareResourceEME("contains/containsAllDict.pec")

    def testContainsAllList(self):
        self.compareResourceEME("contains/containsAllList.pec")

    def testContainsAllRange(self):
        self.compareResourceEME("contains/containsAllRange.pec")

    def testContainsAllSet(self):
        self.compareResourceEME("contains/containsAllSet.pec")

    def testContainsAllText(self):
        self.compareResourceEME("contains/containsAllText.pec")

    def testContainsAllTuple(self):
        self.compareResourceEME("contains/containsAllTuple.pec")

    def testContainsAnyDict(self):
        self.compareResourceEME("contains/containsAnyDict.pec")

    def testContainsAnyList(self):
        self.compareResourceEME("contains/containsAnyList.pec")

    def testContainsAnyRange(self):
        self.compareResourceEME("contains/containsAnyRange.pec")

    def testContainsAnySet(self):
        self.compareResourceEME("contains/containsAnySet.pec")

    def testContainsAnyText(self):
        self.compareResourceEME("contains/containsAnyText.pec")

    def testContainsAnyTuple(self):
        self.compareResourceEME("contains/containsAnyTuple.pec")

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


