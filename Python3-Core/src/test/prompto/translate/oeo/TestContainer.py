from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestContains(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testHasAllList(self):
        self.compareResourceOEO("contains/hasAllList.poc")

    def testHasAllSet(self):
        self.compareResourceOEO("contains/hasAllSet.poc")

    def testHasAllText(self):
        self.compareResourceOEO("contains/hasAllText.poc")

    def testHasAllTuple(self):
        self.compareResourceOEO("contains/hasAllTuple.poc")

    def testHasAnyList(self):
        self.compareResourceOEO("contains/hasAnyList.poc")

    def testHasAnySet(self):
        self.compareResourceOEO("contains/hasAnySet.poc")

    def testHasAnyText(self):
        self.compareResourceOEO("contains/hasAnyText.poc")

    def testHasAnyTuple(self):
        self.compareResourceOEO("contains/hasAnyTuple.poc")

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


