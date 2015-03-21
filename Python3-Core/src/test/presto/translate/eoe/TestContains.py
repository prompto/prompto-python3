from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestContains(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testContainsAllList(self):
        self.compareResourceEOE("contains/containsAllList.e")

    def testContainsAllSet(self):
        self.compareResourceEOE("contains/containsAllSet.e")

    def testContainsAllText(self):
        self.compareResourceEOE("contains/containsAllText.e")

    def testContainsAllTuple(self):
        self.compareResourceEOE("contains/containsAllTuple.e")

    def testContainsAnyList(self):
        self.compareResourceEOE("contains/containsAnyList.e")

    def testContainsAnySet(self):
        self.compareResourceEOE("contains/containsAnySet.e")

    def testContainsAnyText(self):
        self.compareResourceEOE("contains/containsAnyText.e")

    def testContainsAnyTuple(self):
        self.compareResourceEOE("contains/containsAnyTuple.e")

    def testInCharacterRange(self):
        self.compareResourceEOE("contains/inCharacterRange.e")

    def testInDateRange(self):
        self.compareResourceEOE("contains/inDateRange.e")

    def testInDict(self):
        self.compareResourceEOE("contains/inDict.e")

    def testInIntegerRange(self):
        self.compareResourceEOE("contains/inIntegerRange.e")

    def testInList(self):
        self.compareResourceEOE("contains/inList.e")

    def testInSet(self):
        self.compareResourceEOE("contains/inSet.e")

    def testInText(self):
        self.compareResourceEOE("contains/inText.e")

    def testInTimeRange(self):
        self.compareResourceEOE("contains/inTimeRange.e")

    def testInTuple(self):
        self.compareResourceEOE("contains/inTuple.e")

    def testNinCharacterRange(self):
        self.compareResourceEOE("contains/ninCharacterRange.e")

    def testNinDateRange(self):
        self.compareResourceEOE("contains/ninDateRange.e")

    def testNinDict(self):
        self.compareResourceEOE("contains/ninDict.e")

    def testNinIntegerRange(self):
        self.compareResourceEOE("contains/ninIntegerRange.e")

    def testNinList(self):
        self.compareResourceEOE("contains/ninList.e")

    def testNinSet(self):
        self.compareResourceEOE("contains/ninSet.e")

    def testNinText(self):
        self.compareResourceEOE("contains/ninText.e")

    def testNinTimeRange(self):
        self.compareResourceEOE("contains/ninTimeRange.e")


