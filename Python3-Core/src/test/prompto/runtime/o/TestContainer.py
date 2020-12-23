from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestContainer(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testHasAllFromList(self):
        self.checkOutput("container/hasAllFromList.poc")

    def testHasAllFromSet(self):
        self.checkOutput("container/hasAllFromSet.poc")

    def testHasAllList(self):
        self.checkOutput("container/hasAllList.poc")

    def testHasAllSet(self):
        self.checkOutput("container/hasAllSet.poc")

    def testHasAllText(self):
        self.checkOutput("container/hasAllText.poc")

    def testHasAllTuple(self):
        self.checkOutput("container/hasAllTuple.poc")

    def testHasAnyFromList(self):
        self.checkOutput("container/hasAnyFromList.poc")

    def testHasAnyFromSet(self):
        self.checkOutput("container/hasAnyFromSet.poc")

    def testHasAnyList(self):
        self.checkOutput("container/hasAnyList.poc")

    def testHasAnySet(self):
        self.checkOutput("container/hasAnySet.poc")

    def testHasAnyText(self):
        self.checkOutput("container/hasAnyText.poc")

    def testHasAnyTuple(self):
        self.checkOutput("container/hasAnyTuple.poc")

    def testInCharacterRange(self):
        self.checkOutput("container/inCharacterRange.poc")

    def testInDateRange(self):
        self.checkOutput("container/inDateRange.poc")

    def testInDict(self):
        self.checkOutput("container/inDict.poc")

    def testInIntegerRange(self):
        self.checkOutput("container/inIntegerRange.poc")

    def testInList(self):
        self.checkOutput("container/inList.poc")

    def testInSet(self):
        self.checkOutput("container/inSet.poc")

    def testInText(self):
        self.checkOutput("container/inText.poc")

    def testInTextEnum(self):
        self.checkOutput("container/inTextEnum.poc")

    def testInTimeRange(self):
        self.checkOutput("container/inTimeRange.poc")

    def testInTuple(self):
        self.checkOutput("container/inTuple.poc")

    def testNinCharacterRange(self):
        self.checkOutput("container/ninCharacterRange.poc")

    def testNinDateRange(self):
        self.checkOutput("container/ninDateRange.poc")

    def testNinDict(self):
        self.checkOutput("container/ninDict.poc")

    def testNinIntegerRange(self):
        self.checkOutput("container/ninIntegerRange.poc")

    def testNinList(self):
        self.checkOutput("container/ninList.poc")

    def testNinSet(self):
        self.checkOutput("container/ninSet.poc")

    def testNinText(self):
        self.checkOutput("container/ninText.poc")

    def testNinTimeRange(self):
        self.checkOutput("container/ninTimeRange.poc")


