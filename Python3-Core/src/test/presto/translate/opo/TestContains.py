from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestContains(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testContainsAllList(self):
        self.compareResourceOPO("contains/containsAllList.o")

    def testContainsAllSet(self):
        self.compareResourceOPO("contains/containsAllSet.o")

    def testContainsAllText(self):
        self.compareResourceOPO("contains/containsAllText.o")

    def testContainsAllTuple(self):
        self.compareResourceOPO("contains/containsAllTuple.o")

    def testContainsAnyList(self):
        self.compareResourceOPO("contains/containsAnyList.o")

    def testContainsAnySet(self):
        self.compareResourceOPO("contains/containsAnySet.o")

    def testContainsAnyText(self):
        self.compareResourceOPO("contains/containsAnyText.o")

    def testContainsAnyTuple(self):
        self.compareResourceOPO("contains/containsAnyTuple.o")

    def testInCharacterRange(self):
        self.compareResourceOPO("contains/inCharacterRange.o")

    def testInDateRange(self):
        self.compareResourceOPO("contains/inDateRange.o")

    def testInDict(self):
        self.compareResourceOPO("contains/inDict.o")

    def testInIntegerRange(self):
        self.compareResourceOPO("contains/inIntegerRange.o")

    def testInList(self):
        self.compareResourceOPO("contains/inList.o")

    def testInSet(self):
        self.compareResourceOPO("contains/inSet.o")

    def testInText(self):
        self.compareResourceOPO("contains/inText.o")

    def testInTimeRange(self):
        self.compareResourceOPO("contains/inTimeRange.o")

    def testInTuple(self):
        self.compareResourceOPO("contains/inTuple.o")

    def testNinCharacterRange(self):
        self.compareResourceOPO("contains/ninCharacterRange.o")

    def testNinDateRange(self):
        self.compareResourceOPO("contains/ninDateRange.o")

    def testNinDict(self):
        self.compareResourceOPO("contains/ninDict.o")

    def testNinIntegerRange(self):
        self.compareResourceOPO("contains/ninIntegerRange.o")

    def testNinList(self):
        self.compareResourceOPO("contains/ninList.o")

    def testNinSet(self):
        self.compareResourceOPO("contains/ninSet.o")

    def testNinText(self):
        self.compareResourceOPO("contains/ninText.o")

    def testNinTimeRange(self):
        self.compareResourceOPO("contains/ninTimeRange.o")


