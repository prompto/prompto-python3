from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestContains(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testContainsAllList(self):
        self.compareResourceEOE("contains/containsAllList.pec")

    def testContainsAllSet(self):
        self.compareResourceEOE("contains/containsAllSet.pec")

    def testContainsAllText(self):
        self.compareResourceEOE("contains/containsAllText.pec")

    def testContainsAllTuple(self):
        self.compareResourceEOE("contains/containsAllTuple.pec")

    def testContainsAnyList(self):
        self.compareResourceEOE("contains/containsAnyList.pec")

    def testContainsAnySet(self):
        self.compareResourceEOE("contains/containsAnySet.pec")

    def testContainsAnyText(self):
        self.compareResourceEOE("contains/containsAnyText.pec")

    def testContainsAnyTuple(self):
        self.compareResourceEOE("contains/containsAnyTuple.pec")

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


