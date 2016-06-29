from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestContains(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testContainsAllList(self):
        self.checkOutput("contains/containsAllList.pec")

    def testContainsAllRange(self):
        self.checkOutput("contains/containsAllRange.pec")

    def testContainsAllSet(self):
        self.checkOutput("contains/containsAllSet.pec")

    def testContainsAllText(self):
        self.checkOutput("contains/containsAllText.pec")

    def testContainsAllTuple(self):
        self.checkOutput("contains/containsAllTuple.pec")

    def testContainsAnyList(self):
        self.checkOutput("contains/containsAnyList.pec")

    def testContainsAnyRange(self):
        self.checkOutput("contains/containsAnyRange.pec")

    def testContainsAnySet(self):
        self.checkOutput("contains/containsAnySet.pec")

    def testContainsAnyText(self):
        self.checkOutput("contains/containsAnyText.pec")

    def testContainsAnyTuple(self):
        self.checkOutput("contains/containsAnyTuple.pec")

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


