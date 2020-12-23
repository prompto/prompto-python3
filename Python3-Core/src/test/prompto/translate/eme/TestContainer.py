from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestContainer(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testHasAllDict(self):
        self.compareResourceEME("container/hasAllDict.pec")

    def testHasAllFromList(self):
        self.compareResourceEME("container/hasAllFromList.pec")

    def testHasAllFromSet(self):
        self.compareResourceEME("container/hasAllFromSet.pec")

    def testHasAllList(self):
        self.compareResourceEME("container/hasAllList.pec")

    def testHasAllRange(self):
        self.compareResourceEME("container/hasAllRange.pec")

    def testHasAllSet(self):
        self.compareResourceEME("container/hasAllSet.pec")

    def testHasAllText(self):
        self.compareResourceEME("container/hasAllText.pec")

    def testHasAllTuple(self):
        self.compareResourceEME("container/hasAllTuple.pec")

    def testHasAnyDict(self):
        self.compareResourceEME("container/hasAnyDict.pec")

    def testHasAnyFromList(self):
        self.compareResourceEME("container/hasAnyFromList.pec")

    def testHasAnyFromSet(self):
        self.compareResourceEME("container/hasAnyFromSet.pec")

    def testHasAnyList(self):
        self.compareResourceEME("container/hasAnyList.pec")

    def testHasAnyRange(self):
        self.compareResourceEME("container/hasAnyRange.pec")

    def testHasAnySet(self):
        self.compareResourceEME("container/hasAnySet.pec")

    def testHasAnyText(self):
        self.compareResourceEME("container/hasAnyText.pec")

    def testHasAnyTuple(self):
        self.compareResourceEME("container/hasAnyTuple.pec")

    def testInCharacterRange(self):
        self.compareResourceEME("container/inCharacterRange.pec")

    def testInDateRange(self):
        self.compareResourceEME("container/inDateRange.pec")

    def testInDict(self):
        self.compareResourceEME("container/inDict.pec")

    def testInIntegerRange(self):
        self.compareResourceEME("container/inIntegerRange.pec")

    def testInList(self):
        self.compareResourceEME("container/inList.pec")

    def testInSet(self):
        self.compareResourceEME("container/inSet.pec")

    def testInText(self):
        self.compareResourceEME("container/inText.pec")

    def testInTextEnum(self):
        self.compareResourceEME("container/inTextEnum.pec")

    def testInTimeRange(self):
        self.compareResourceEME("container/inTimeRange.pec")

    def testInTuple(self):
        self.compareResourceEME("container/inTuple.pec")

    def testNinCharacterRange(self):
        self.compareResourceEME("container/ninCharacterRange.pec")

    def testNinDateRange(self):
        self.compareResourceEME("container/ninDateRange.pec")

    def testNinDict(self):
        self.compareResourceEME("container/ninDict.pec")

    def testNinIntegerRange(self):
        self.compareResourceEME("container/ninIntegerRange.pec")

    def testNinList(self):
        self.compareResourceEME("container/ninList.pec")

    def testNinSet(self):
        self.compareResourceEME("container/ninSet.pec")

    def testNinText(self):
        self.compareResourceEME("container/ninText.pec")

    def testNinTimeRange(self):
        self.compareResourceEME("container/ninTimeRange.pec")


