from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestContains(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testContainsAllList(self):
        self.compareResourceOMO("contains/containsAllList.poc")

    def testContainsAllSet(self):
        self.compareResourceOMO("contains/containsAllSet.poc")

    def testContainsAllText(self):
        self.compareResourceOMO("contains/containsAllText.poc")

    def testContainsAllTuple(self):
        self.compareResourceOMO("contains/containsAllTuple.poc")

    def testContainsAnyList(self):
        self.compareResourceOMO("contains/containsAnyList.poc")

    def testContainsAnySet(self):
        self.compareResourceOMO("contains/containsAnySet.poc")

    def testContainsAnyText(self):
        self.compareResourceOMO("contains/containsAnyText.poc")

    def testContainsAnyTuple(self):
        self.compareResourceOMO("contains/containsAnyTuple.poc")

    def testInCharacterRange(self):
        self.compareResourceOMO("contains/inCharacterRange.poc")

    def testInDateRange(self):
        self.compareResourceOMO("contains/inDateRange.poc")

    def testInDict(self):
        self.compareResourceOMO("contains/inDict.poc")

    def testInIntegerRange(self):
        self.compareResourceOMO("contains/inIntegerRange.poc")

    def testInList(self):
        self.compareResourceOMO("contains/inList.poc")

    def testInSet(self):
        self.compareResourceOMO("contains/inSet.poc")

    def testInText(self):
        self.compareResourceOMO("contains/inText.poc")

    def testInTimeRange(self):
        self.compareResourceOMO("contains/inTimeRange.poc")

    def testInTuple(self):
        self.compareResourceOMO("contains/inTuple.poc")

    def testNinCharacterRange(self):
        self.compareResourceOMO("contains/ninCharacterRange.poc")

    def testNinDateRange(self):
        self.compareResourceOMO("contains/ninDateRange.poc")

    def testNinDict(self):
        self.compareResourceOMO("contains/ninDict.poc")

    def testNinIntegerRange(self):
        self.compareResourceOMO("contains/ninIntegerRange.poc")

    def testNinList(self):
        self.compareResourceOMO("contains/ninList.poc")

    def testNinSet(self):
        self.compareResourceOMO("contains/ninSet.poc")

    def testNinText(self):
        self.compareResourceOMO("contains/ninText.poc")

    def testNinTimeRange(self):
        self.compareResourceOMO("contains/ninTimeRange.poc")


