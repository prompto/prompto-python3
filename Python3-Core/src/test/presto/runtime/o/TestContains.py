from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestContains(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testContainsAllList(self):
        self.checkOutput("contains/containsAllList.o")

    def testContainsAllSet(self):
        self.checkOutput("contains/containsAllSet.o")

    def testContainsAllText(self):
        self.checkOutput("contains/containsAllText.o")

    def testContainsAllTuple(self):
        self.checkOutput("contains/containsAllTuple.o")

    def testContainsAnyList(self):
        self.checkOutput("contains/containsAnyList.o")

    def testContainsAnySet(self):
        self.checkOutput("contains/containsAnySet.o")

    def testContainsAnyText(self):
        self.checkOutput("contains/containsAnyText.o")

    def testContainsAnyTuple(self):
        self.checkOutput("contains/containsAnyTuple.o")

    def testInCharacterRange(self):
        self.checkOutput("contains/inCharacterRange.o")

    def testInDateRange(self):
        self.checkOutput("contains/inDateRange.o")

    def testInDict(self):
        self.checkOutput("contains/inDict.o")

    def testInIntegerRange(self):
        self.checkOutput("contains/inIntegerRange.o")

    def testInList(self):
        self.checkOutput("contains/inList.o")

    def testInSet(self):
        self.checkOutput("contains/inSet.o")

    def testInText(self):
        self.checkOutput("contains/inText.o")

    def testInTimeRange(self):
        self.checkOutput("contains/inTimeRange.o")

    def testInTuple(self):
        self.checkOutput("contains/inTuple.o")

    def testNinCharacterRange(self):
        self.checkOutput("contains/ninCharacterRange.o")

    def testNinDateRange(self):
        self.checkOutput("contains/ninDateRange.o")

    def testNinDict(self):
        self.checkOutput("contains/ninDict.o")

    def testNinIntegerRange(self):
        self.checkOutput("contains/ninIntegerRange.o")

    def testNinList(self):
        self.checkOutput("contains/ninList.o")

    def testNinSet(self):
        self.checkOutput("contains/ninSet.o")

    def testNinText(self):
        self.checkOutput("contains/ninText.o")

    def testNinTimeRange(self):
        self.checkOutput("contains/ninTimeRange.o")


