from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestContains(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testContainsAllList(self):
        self.checkOutput("contains/containsAllList.e")

    def testContainsAllSet(self):
        self.checkOutput("contains/containsAllSet.e")

    def testContainsAllText(self):
        self.checkOutput("contains/containsAllText.e")

    def testContainsAllTuple(self):
        self.checkOutput("contains/containsAllTuple.e")

    def testContainsAnyList(self):
        self.checkOutput("contains/containsAnyList.e")

    def testContainsAnySet(self):
        self.checkOutput("contains/containsAnySet.e")

    def testContainsAnyText(self):
        self.checkOutput("contains/containsAnyText.e")

    def testContainsAnyTuple(self):
        self.checkOutput("contains/containsAnyTuple.e")

    def testInCharacterRange(self):
        self.checkOutput("contains/inCharacterRange.e")

    def testInDateRange(self):
        self.checkOutput("contains/inDateRange.e")

    def testInDict(self):
        self.checkOutput("contains/inDict.e")

    def testInIntegerRange(self):
        self.checkOutput("contains/inIntegerRange.e")

    def testInList(self):
        self.checkOutput("contains/inList.e")

    def testInSet(self):
        self.checkOutput("contains/inSet.e")

    def testInText(self):
        self.checkOutput("contains/inText.e")

    def testInTimeRange(self):
        self.checkOutput("contains/inTimeRange.e")

    def testInTuple(self):
        self.checkOutput("contains/inTuple.e")

    def testNinCharacterRange(self):
        self.checkOutput("contains/ninCharacterRange.e")

    def testNinDateRange(self):
        self.checkOutput("contains/ninDateRange.e")

    def testNinDict(self):
        self.checkOutput("contains/ninDict.e")

    def testNinIntegerRange(self):
        self.checkOutput("contains/ninIntegerRange.e")

    def testNinList(self):
        self.checkOutput("contains/ninList.e")

    def testNinSet(self):
        self.checkOutput("contains/ninSet.e")

    def testNinText(self):
        self.checkOutput("contains/ninText.e")

    def testNinTimeRange(self):
        self.checkOutput("contains/ninTimeRange.e")


