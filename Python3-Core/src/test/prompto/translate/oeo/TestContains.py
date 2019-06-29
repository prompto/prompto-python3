from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestContains(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testContainsAllList(self):
        self.compareResourceOEO("contains/containsAllList.poc")

    def testContainsAllSet(self):
        self.compareResourceOEO("contains/containsAllSet.poc")

    def testContainsAllText(self):
        self.compareResourceOEO("contains/containsAllText.poc")

    def testContainsAllTuple(self):
        self.compareResourceOEO("contains/containsAllTuple.poc")

    def testContainsAnyList(self):
        self.compareResourceOEO("contains/containsAnyList.poc")

    def testContainsAnySet(self):
        self.compareResourceOEO("contains/containsAnySet.poc")

    def testContainsAnyText(self):
        self.compareResourceOEO("contains/containsAnyText.poc")

    def testContainsAnyTuple(self):
        self.compareResourceOEO("contains/containsAnyTuple.poc")

    def testInCharacterRange(self):
        self.compareResourceOEO("contains/inCharacterRange.poc")

    def testInDateRange(self):
        self.compareResourceOEO("contains/inDateRange.poc")

    def testInDict(self):
        self.compareResourceOEO("contains/inDict.poc")

    def testInIntegerRange(self):
        self.compareResourceOEO("contains/inIntegerRange.poc")

    def testInList(self):
        self.compareResourceOEO("contains/inList.poc")

    def testInSet(self):
        self.compareResourceOEO("contains/inSet.poc")

    def testInText(self):
        self.compareResourceOEO("contains/inText.poc")

    def testInTextEnum(self):
        self.compareResourceOEO("contains/inTextEnum.poc")

    def testInTimeRange(self):
        self.compareResourceOEO("contains/inTimeRange.poc")

    def testInTuple(self):
        self.compareResourceOEO("contains/inTuple.poc")

    def testNinCharacterRange(self):
        self.compareResourceOEO("contains/ninCharacterRange.poc")

    def testNinDateRange(self):
        self.compareResourceOEO("contains/ninDateRange.poc")

    def testNinDict(self):
        self.compareResourceOEO("contains/ninDict.poc")

    def testNinIntegerRange(self):
        self.compareResourceOEO("contains/ninIntegerRange.poc")

    def testNinList(self):
        self.compareResourceOEO("contains/ninList.poc")

    def testNinSet(self):
        self.compareResourceOEO("contains/ninSet.poc")

    def testNinText(self):
        self.compareResourceOEO("contains/ninText.poc")

    def testNinTimeRange(self):
        self.compareResourceOEO("contains/ninTimeRange.poc")


