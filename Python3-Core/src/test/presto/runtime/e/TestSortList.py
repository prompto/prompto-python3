from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestSortList(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSortBooleans(self):
        self.checkOutput("sortList/sortBooleans.e")

    def testSortDates(self):
        self.checkOutput("sortList/sortDates.e")

    def testSortDateTimes(self):
        self.checkOutput("sortList/sortDateTimes.e")

    def testSortDecimals(self):
        self.checkOutput("sortList/sortDecimals.e")

    def testSortExpressions(self):
        self.checkOutput("sortList/sortExpressions.e")

    def testSortIntegers(self):
        self.checkOutput("sortList/sortIntegers.e")

    def testSortKeys(self):
        self.checkOutput("sortList/sortKeys.e")

    def testSortMethods(self):
        self.checkOutput("sortList/sortMethods.e")

    def testSortNames(self):
        self.checkOutput("sortList/sortNames.e")

    def testSortTexts(self):
        self.checkOutput("sortList/sortTexts.e")

    def testSortTimes(self):
        self.checkOutput("sortList/sortTimes.e")


