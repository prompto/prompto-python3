from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestContains(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testContainsAllList(self):
        self.compareResourceOEO("contains/containsAllList.o")

    def testContainsAllSet(self):
        self.compareResourceOEO("contains/containsAllSet.o")

    def testContainsAllText(self):
        self.compareResourceOEO("contains/containsAllText.o")

    def testContainsAllTuple(self):
        self.compareResourceOEO("contains/containsAllTuple.o")

    def testContainsAnyList(self):
        self.compareResourceOEO("contains/containsAnyList.o")

    def testContainsAnySet(self):
        self.compareResourceOEO("contains/containsAnySet.o")

    def testContainsAnyText(self):
        self.compareResourceOEO("contains/containsAnyText.o")

    def testContainsAnyTuple(self):
        self.compareResourceOEO("contains/containsAnyTuple.o")

    def testInCharacterRange(self):
        self.compareResourceOEO("contains/inCharacterRange.o")

    def testInDateRange(self):
        self.compareResourceOEO("contains/inDateRange.o")

    def testInDict(self):
        self.compareResourceOEO("contains/inDict.o")

    def testInIntegerRange(self):
        self.compareResourceOEO("contains/inIntegerRange.o")

    def testInList(self):
        self.compareResourceOEO("contains/inList.o")

    def testInSet(self):
        self.compareResourceOEO("contains/inSet.o")

    def testInText(self):
        self.compareResourceOEO("contains/inText.o")

    def testInTimeRange(self):
        self.compareResourceOEO("contains/inTimeRange.o")

    def testInTuple(self):
        self.compareResourceOEO("contains/inTuple.o")

    def testNinCharacterRange(self):
        self.compareResourceOEO("contains/ninCharacterRange.o")

    def testNinDateRange(self):
        self.compareResourceOEO("contains/ninDateRange.o")

    def testNinDict(self):
        self.compareResourceOEO("contains/ninDict.o")

    def testNinIntegerRange(self):
        self.compareResourceOEO("contains/ninIntegerRange.o")

    def testNinList(self):
        self.compareResourceOEO("contains/ninList.o")

    def testNinSet(self):
        self.compareResourceOEO("contains/ninSet.o")

    def testNinText(self):
        self.compareResourceOEO("contains/ninText.o")

    def testNinTimeRange(self):
        self.compareResourceOEO("contains/ninTimeRange.o")


