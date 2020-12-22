from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestContains(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testHasAllDict(self):
        self.checkOutput("contains/hasAllDict.pec")

    def testHasAllList(self):
        self.checkOutput("contains/hasAllList.pec")

    def testHasAllRange(self):
        self.checkOutput("contains/hasAllRange.pec")

    def testHasAllSet(self):
        self.checkOutput("contains/hasAllSet.pec")

    def testHasAllText(self):
        self.checkOutput("contains/hasAllText.pec")

    def testHasAllTuple(self):
        self.checkOutput("contains/hasAllTuple.pec")

    def testHasAnyDict(self):
        self.checkOutput("contains/hasAnyDict.pec")

    def testHasAnyList(self):
        self.checkOutput("contains/hasAnyList.pec")

    def testHasAnyRange(self):
        self.checkOutput("contains/hasAnyRange.pec")

    def testHasAnySet(self):
        self.checkOutput("contains/hasAnySet.pec")

    def testHasAnyText(self):
        self.checkOutput("contains/hasAnyText.pec")

    def testHasAnyTuple(self):
        self.checkOutput("contains/hasAnyTuple.pec")

    def testInCharacterRange(self):
        self.checkOutput("contains/inCharacterRange.pec")

    def testInDateRange(self):
        self.checkOutput("contains/inDateRange.pec")

    def testInDict(self):
        self.checkOutput("contains/inDict.pec")

    def testInIntegerRange(self):
        self.checkOutput("contains/inIntegerRange.pec")

    def testInList(self):
        self.checkOutput("contains/inList.pec")

    def testInSet(self):
        self.checkOutput("contains/inSet.pec")

    def testInText(self):
        self.checkOutput("contains/inText.pec")

    def testInTextEnum(self):
        self.checkOutput("contains/inTextEnum.pec")

    def testInTimeRange(self):
        self.checkOutput("contains/inTimeRange.pec")

    def testInTuple(self):
        self.checkOutput("contains/inTuple.pec")

    def testNinCharacterRange(self):
        self.checkOutput("contains/ninCharacterRange.pec")

    def testNinDateRange(self):
        self.checkOutput("contains/ninDateRange.pec")

    def testNinDict(self):
        self.checkOutput("contains/ninDict.pec")

    def testNinIntegerRange(self):
        self.checkOutput("contains/ninIntegerRange.pec")

    def testNinList(self):
        self.checkOutput("contains/ninList.pec")

    def testNinSet(self):
        self.checkOutput("contains/ninSet.pec")

    def testNinText(self):
        self.checkOutput("contains/ninText.pec")

    def testNinTimeRange(self):
        self.checkOutput("contains/ninTimeRange.pec")


