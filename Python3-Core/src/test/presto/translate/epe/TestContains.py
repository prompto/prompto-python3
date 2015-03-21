from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestContains(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testContainsAllList(self):
        self.compareResourceEPE("contains/containsAllList.e")

    def testContainsAllSet(self):
        self.compareResourceEPE("contains/containsAllSet.e")

    def testContainsAllText(self):
        self.compareResourceEPE("contains/containsAllText.e")

    def testContainsAllTuple(self):
        self.compareResourceEPE("contains/containsAllTuple.e")

    def testContainsAnyList(self):
        self.compareResourceEPE("contains/containsAnyList.e")

    def testContainsAnySet(self):
        self.compareResourceEPE("contains/containsAnySet.e")

    def testContainsAnyText(self):
        self.compareResourceEPE("contains/containsAnyText.e")

    def testContainsAnyTuple(self):
        self.compareResourceEPE("contains/containsAnyTuple.e")

    def testInCharacterRange(self):
        self.compareResourceEPE("contains/inCharacterRange.e")

    def testInDateRange(self):
        self.compareResourceEPE("contains/inDateRange.e")

    def testInDict(self):
        self.compareResourceEPE("contains/inDict.e")

    def testInIntegerRange(self):
        self.compareResourceEPE("contains/inIntegerRange.e")

    def testInList(self):
        self.compareResourceEPE("contains/inList.e")

    def testInSet(self):
        self.compareResourceEPE("contains/inSet.e")

    def testInText(self):
        self.compareResourceEPE("contains/inText.e")

    def testInTimeRange(self):
        self.compareResourceEPE("contains/inTimeRange.e")

    def testInTuple(self):
        self.compareResourceEPE("contains/inTuple.e")

    def testNinCharacterRange(self):
        self.compareResourceEPE("contains/ninCharacterRange.e")

    def testNinDateRange(self):
        self.compareResourceEPE("contains/ninDateRange.e")

    def testNinDict(self):
        self.compareResourceEPE("contains/ninDict.e")

    def testNinIntegerRange(self):
        self.compareResourceEPE("contains/ninIntegerRange.e")

    def testNinList(self):
        self.compareResourceEPE("contains/ninList.e")

    def testNinSet(self):
        self.compareResourceEPE("contains/ninSet.e")

    def testNinText(self):
        self.compareResourceEPE("contains/ninText.e")

    def testNinTimeRange(self):
        self.compareResourceEPE("contains/ninTimeRange.e")


