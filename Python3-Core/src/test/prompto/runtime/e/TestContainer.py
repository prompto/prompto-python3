from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestContainer(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testHasAllDict(self):
        self.checkOutput("container/hasAllDict.pec")

    def testHasAllList(self):
        self.checkOutput("container/hasAllList.pec")

    def testHasAllRange(self):
        self.checkOutput("container/hasAllRange.pec")

    def testHasAllSet(self):
        self.checkOutput("container/hasAllSet.pec")

    def testHasAllText(self):
        self.checkOutput("container/hasAllText.pec")

    def testHasAllTuple(self):
        self.checkOutput("container/hasAllTuple.pec")

    def testHasAnyDict(self):
        self.checkOutput("container/hasAnyDict.pec")

    def testHasAnyList(self):
        self.checkOutput("container/hasAnyList.pec")

    def testHasAnyRange(self):
        self.checkOutput("container/hasAnyRange.pec")

    def testHasAnySet(self):
        self.checkOutput("container/hasAnySet.pec")

    def testHasAnyText(self):
        self.checkOutput("container/hasAnyText.pec")

    def testHasAnyTuple(self):
        self.checkOutput("container/hasAnyTuple.pec")

    def testInCharacterRange(self):
        self.checkOutput("container/inCharacterRange.pec")

    def testInDateRange(self):
        self.checkOutput("container/inDateRange.pec")

    def testInDict(self):
        self.checkOutput("container/inDict.pec")

    def testInIntegerRange(self):
        self.checkOutput("container/inIntegerRange.pec")

    def testInList(self):
        self.checkOutput("container/inList.pec")

    def testInSet(self):
        self.checkOutput("container/inSet.pec")

    def testInText(self):
        self.checkOutput("container/inText.pec")

    def testInTextEnum(self):
        self.checkOutput("container/inTextEnum.pec")

    def testInTimeRange(self):
        self.checkOutput("container/inTimeRange.pec")

    def testInTuple(self):
        self.checkOutput("container/inTuple.pec")

    def testNinCharacterRange(self):
        self.checkOutput("container/ninCharacterRange.pec")

    def testNinDateRange(self):
        self.checkOutput("container/ninDateRange.pec")

    def testNinDict(self):
        self.checkOutput("container/ninDict.pec")

    def testNinIntegerRange(self):
        self.checkOutput("container/ninIntegerRange.pec")

    def testNinList(self):
        self.checkOutput("container/ninList.pec")

    def testNinSet(self):
        self.checkOutput("container/ninSet.pec")

    def testNinText(self):
        self.checkOutput("container/ninText.pec")

    def testNinTimeRange(self):
        self.checkOutput("container/ninTimeRange.pec")


