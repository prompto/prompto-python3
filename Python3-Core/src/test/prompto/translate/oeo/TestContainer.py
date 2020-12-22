from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestContainer(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testHasAllList(self):
        self.compareResourceOEO("container/hasAllList.poc")

    def testHasAllSet(self):
        self.compareResourceOEO("container/hasAllSet.poc")

    def testHasAllText(self):
        self.compareResourceOEO("container/hasAllText.poc")

    def testHasAllTuple(self):
        self.compareResourceOEO("container/hasAllTuple.poc")

    def testHasAnyList(self):
        self.compareResourceOEO("container/hasAnyList.poc")

    def testHasAnySet(self):
        self.compareResourceOEO("container/hasAnySet.poc")

    def testHasAnyText(self):
        self.compareResourceOEO("container/hasAnyText.poc")

    def testHasAnyTuple(self):
        self.compareResourceOEO("container/hasAnyTuple.poc")

    def testInCharacterRange(self):
        self.compareResourceOEO("container/inCharacterRange.poc")

    def testInDateRange(self):
        self.compareResourceOEO("container/inDateRange.poc")

    def testInDict(self):
        self.compareResourceOEO("container/inDict.poc")

    def testInIntegerRange(self):
        self.compareResourceOEO("container/inIntegerRange.poc")

    def testInList(self):
        self.compareResourceOEO("container/inList.poc")

    def testInSet(self):
        self.compareResourceOEO("container/inSet.poc")

    def testInText(self):
        self.compareResourceOEO("container/inText.poc")

    def testInTextEnum(self):
        self.compareResourceOEO("container/inTextEnum.poc")

    def testInTimeRange(self):
        self.compareResourceOEO("container/inTimeRange.poc")

    def testInTuple(self):
        self.compareResourceOEO("container/inTuple.poc")

    def testNinCharacterRange(self):
        self.compareResourceOEO("container/ninCharacterRange.poc")

    def testNinDateRange(self):
        self.compareResourceOEO("container/ninDateRange.poc")

    def testNinDict(self):
        self.compareResourceOEO("container/ninDict.poc")

    def testNinIntegerRange(self):
        self.compareResourceOEO("container/ninIntegerRange.poc")

    def testNinList(self):
        self.compareResourceOEO("container/ninList.poc")

    def testNinSet(self):
        self.compareResourceOEO("container/ninSet.poc")

    def testNinText(self):
        self.compareResourceOEO("container/ninText.poc")

    def testNinTimeRange(self):
        self.compareResourceOEO("container/ninTimeRange.poc")


