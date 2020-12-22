from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestContainer(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testHasAllDict(self):
        self.compareResourceEOE("container/hasAllDict.pec")

    def testHasAllList(self):
        self.compareResourceEOE("container/hasAllList.pec")

    def testHasAllRange(self):
        self.compareResourceEOE("container/hasAllRange.pec")

    def testHasAllSet(self):
        self.compareResourceEOE("container/hasAllSet.pec")

    def testHasAllText(self):
        self.compareResourceEOE("container/hasAllText.pec")

    def testHasAllTuple(self):
        self.compareResourceEOE("container/hasAllTuple.pec")

    def testHasAnyDict(self):
        self.compareResourceEOE("container/hasAnyDict.pec")

    def testHasAnyList(self):
        self.compareResourceEOE("container/hasAnyList.pec")

    def testHasAnyRange(self):
        self.compareResourceEOE("container/hasAnyRange.pec")

    def testHasAnySet(self):
        self.compareResourceEOE("container/hasAnySet.pec")

    def testHasAnyText(self):
        self.compareResourceEOE("container/hasAnyText.pec")

    def testHasAnyTuple(self):
        self.compareResourceEOE("container/hasAnyTuple.pec")

    def testInCharacterRange(self):
        self.compareResourceEOE("container/inCharacterRange.pec")

    def testInDateRange(self):
        self.compareResourceEOE("container/inDateRange.pec")

    def testInDict(self):
        self.compareResourceEOE("container/inDict.pec")

    def testInIntegerRange(self):
        self.compareResourceEOE("container/inIntegerRange.pec")

    def testInList(self):
        self.compareResourceEOE("container/inList.pec")

    def testInSet(self):
        self.compareResourceEOE("container/inSet.pec")

    def testInText(self):
        self.compareResourceEOE("container/inText.pec")

    def testInTextEnum(self):
        self.compareResourceEOE("container/inTextEnum.pec")

    def testInTimeRange(self):
        self.compareResourceEOE("container/inTimeRange.pec")

    def testInTuple(self):
        self.compareResourceEOE("container/inTuple.pec")

    def testNinCharacterRange(self):
        self.compareResourceEOE("container/ninCharacterRange.pec")

    def testNinDateRange(self):
        self.compareResourceEOE("container/ninDateRange.pec")

    def testNinDict(self):
        self.compareResourceEOE("container/ninDict.pec")

    def testNinIntegerRange(self):
        self.compareResourceEOE("container/ninIntegerRange.pec")

    def testNinList(self):
        self.compareResourceEOE("container/ninList.pec")

    def testNinSet(self):
        self.compareResourceEOE("container/ninSet.pec")

    def testNinText(self):
        self.compareResourceEOE("container/ninText.pec")

    def testNinTimeRange(self):
        self.compareResourceEOE("container/ninTimeRange.pec")


