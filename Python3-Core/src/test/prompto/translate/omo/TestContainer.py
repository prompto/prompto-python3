from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestContainer(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testHasAllFromList(self):
        self.compareResourceOMO("container/hasAllFromList.poc")

    def testHasAllFromSet(self):
        self.compareResourceOMO("container/hasAllFromSet.poc")

    def testHasAllList(self):
        self.compareResourceOMO("container/hasAllList.poc")

    def testHasAllSet(self):
        self.compareResourceOMO("container/hasAllSet.poc")

    def testHasAllText(self):
        self.compareResourceOMO("container/hasAllText.poc")

    def testHasAllTuple(self):
        self.compareResourceOMO("container/hasAllTuple.poc")

    def testHasAnyFromList(self):
        self.compareResourceOMO("container/hasAnyFromList.poc")

    def testHasAnyFromSet(self):
        self.compareResourceOMO("container/hasAnyFromSet.poc")

    def testHasAnyList(self):
        self.compareResourceOMO("container/hasAnyList.poc")

    def testHasAnySet(self):
        self.compareResourceOMO("container/hasAnySet.poc")

    def testHasAnyText(self):
        self.compareResourceOMO("container/hasAnyText.poc")

    def testHasAnyTuple(self):
        self.compareResourceOMO("container/hasAnyTuple.poc")

    def testInCharacterRange(self):
        self.compareResourceOMO("container/inCharacterRange.poc")

    def testInDateRange(self):
        self.compareResourceOMO("container/inDateRange.poc")

    def testInDict(self):
        self.compareResourceOMO("container/inDict.poc")

    def testInIntegerRange(self):
        self.compareResourceOMO("container/inIntegerRange.poc")

    def testInList(self):
        self.compareResourceOMO("container/inList.poc")

    def testInSet(self):
        self.compareResourceOMO("container/inSet.poc")

    def testInText(self):
        self.compareResourceOMO("container/inText.poc")

    def testInTextEnum(self):
        self.compareResourceOMO("container/inTextEnum.poc")

    def testInTimeRange(self):
        self.compareResourceOMO("container/inTimeRange.poc")

    def testInTuple(self):
        self.compareResourceOMO("container/inTuple.poc")

    def testNinCharacterRange(self):
        self.compareResourceOMO("container/ninCharacterRange.poc")

    def testNinDateRange(self):
        self.compareResourceOMO("container/ninDateRange.poc")

    def testNinDict(self):
        self.compareResourceOMO("container/ninDict.poc")

    def testNinIntegerRange(self):
        self.compareResourceOMO("container/ninIntegerRange.poc")

    def testNinList(self):
        self.compareResourceOMO("container/ninList.poc")

    def testNinSet(self):
        self.compareResourceOMO("container/ninSet.poc")

    def testNinText(self):
        self.compareResourceOMO("container/ninText.poc")

    def testNinTimeRange(self):
        self.compareResourceOMO("container/ninTimeRange.poc")


