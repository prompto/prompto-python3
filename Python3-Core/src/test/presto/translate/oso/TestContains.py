from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestContains(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testContainsAllList(self):
        self.compareResourceOSO("contains/containsAllList.poc")

    def testContainsAllSet(self):
        self.compareResourceOSO("contains/containsAllSet.poc")

    def testContainsAllText(self):
        self.compareResourceOSO("contains/containsAllText.poc")

    def testContainsAllTuple(self):
        self.compareResourceOSO("contains/containsAllTuple.poc")

    def testContainsAnyList(self):
        self.compareResourceOSO("contains/containsAnyList.poc")

    def testContainsAnySet(self):
        self.compareResourceOSO("contains/containsAnySet.poc")

    def testContainsAnyText(self):
        self.compareResourceOSO("contains/containsAnyText.poc")

    def testContainsAnyTuple(self):
        self.compareResourceOSO("contains/containsAnyTuple.poc")

    def testInCharacterRange(self):
        self.compareResourceOSO("contains/inCharacterRange.poc")

    def testInDateRange(self):
        self.compareResourceOSO("contains/inDateRange.poc")

    def testInDict(self):
        self.compareResourceOSO("contains/inDict.poc")

    def testInIntegerRange(self):
        self.compareResourceOSO("contains/inIntegerRange.poc")

    def testInList(self):
        self.compareResourceOSO("contains/inList.poc")

    def testInSet(self):
        self.compareResourceOSO("contains/inSet.poc")

    def testInText(self):
        self.compareResourceOSO("contains/inText.poc")

    def testInTimeRange(self):
        self.compareResourceOSO("contains/inTimeRange.poc")

    def testInTuple(self):
        self.compareResourceOSO("contains/inTuple.poc")

    def testNinCharacterRange(self):
        self.compareResourceOSO("contains/ninCharacterRange.poc")

    def testNinDateRange(self):
        self.compareResourceOSO("contains/ninDateRange.poc")

    def testNinDict(self):
        self.compareResourceOSO("contains/ninDict.poc")

    def testNinIntegerRange(self):
        self.compareResourceOSO("contains/ninIntegerRange.poc")

    def testNinList(self):
        self.compareResourceOSO("contains/ninList.poc")

    def testNinSet(self):
        self.compareResourceOSO("contains/ninSet.poc")

    def testNinText(self):
        self.compareResourceOSO("contains/ninText.poc")

    def testNinTimeRange(self):
        self.compareResourceOSO("contains/ninTimeRange.poc")


