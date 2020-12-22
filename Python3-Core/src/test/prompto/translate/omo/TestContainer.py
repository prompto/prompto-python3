from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestContains(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testHasAllList(self):
        self.compareResourceOMO("contains/hasAllList.poc")

    def testHasAllSet(self):
        self.compareResourceOMO("contains/hasAllSet.poc")

    def testHasAllText(self):
        self.compareResourceOMO("contains/hasAllText.poc")

    def testHasAllTuple(self):
        self.compareResourceOMO("contains/hasAllTuple.poc")

    def testHasAnyList(self):
        self.compareResourceOMO("contains/hasAnyList.poc")

    def testHasAnySet(self):
        self.compareResourceOMO("contains/hasAnySet.poc")

    def testHasAnyText(self):
        self.compareResourceOMO("contains/hasAnyText.poc")

    def testHasAnyTuple(self):
        self.compareResourceOMO("contains/hasAnyTuple.poc")

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

    def testInTextEnum(self):
        self.compareResourceOMO("contains/inTextEnum.poc")

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


