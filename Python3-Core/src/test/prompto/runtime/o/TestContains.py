from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestContains(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testContainsAllList(self):
        self.checkOutput("contains/containsAllList.poc")

    def testContainsAllSet(self):
        self.checkOutput("contains/containsAllSet.poc")

    def testContainsAllText(self):
        self.checkOutput("contains/containsAllText.poc")

    def testContainsAllTuple(self):
        self.checkOutput("contains/containsAllTuple.poc")

    def testContainsAnyList(self):
        self.checkOutput("contains/containsAnyList.poc")

    def testContainsAnySet(self):
        self.checkOutput("contains/containsAnySet.poc")

    def testContainsAnyText(self):
        self.checkOutput("contains/containsAnyText.poc")

    def testContainsAnyTuple(self):
        self.checkOutput("contains/containsAnyTuple.poc")

    def testInCharacterRange(self):
        self.checkOutput("contains/inCharacterRange.poc")

    def testInDateRange(self):
        self.checkOutput("contains/inDateRange.poc")

    def testInDict(self):
        self.checkOutput("contains/inDict.poc")

    def testInIntegerRange(self):
        self.checkOutput("contains/inIntegerRange.poc")

    def testInList(self):
        self.checkOutput("contains/inList.poc")

    def testInSet(self):
        self.checkOutput("contains/inSet.poc")

    def testInText(self):
        self.checkOutput("contains/inText.poc")

    def testInTimeRange(self):
        self.checkOutput("contains/inTimeRange.poc")

    def testInTuple(self):
        self.checkOutput("contains/inTuple.poc")

    def testNinCharacterRange(self):
        self.checkOutput("contains/ninCharacterRange.poc")

    def testNinDateRange(self):
        self.checkOutput("contains/ninDateRange.poc")

    def testNinDict(self):
        self.checkOutput("contains/ninDict.poc")

    def testNinIntegerRange(self):
        self.checkOutput("contains/ninIntegerRange.poc")

    def testNinList(self):
        self.checkOutput("contains/ninList.poc")

    def testNinSet(self):
        self.checkOutput("contains/ninSet.poc")

    def testNinText(self):
        self.checkOutput("contains/ninText.poc")

    def testNinTimeRange(self):
        self.checkOutput("contains/ninTimeRange.poc")


