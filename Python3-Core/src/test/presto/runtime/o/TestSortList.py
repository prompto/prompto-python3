from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestSortList(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSortBooleans(self):
        self.checkOutput("sortList/sortBooleans.poc")

    def testSortDates(self):
        self.checkOutput("sortList/sortDates.poc")

    def testSortDateTimes(self):
        self.checkOutput("sortList/sortDateTimes.poc")

    def testSortDecimals(self):
        self.checkOutput("sortList/sortDecimals.poc")

    def testSortExpressions(self):
        self.checkOutput("sortList/sortExpressions.poc")

    def testSortIntegers(self):
        self.checkOutput("sortList/sortIntegers.poc")

    def testSortKeys(self):
        self.checkOutput("sortList/sortKeys.poc")

    def testSortMethods(self):
        self.checkOutput("sortList/sortMethods.poc")

    def testSortNames(self):
        self.checkOutput("sortList/sortNames.poc")

    def testSortTexts(self):
        self.checkOutput("sortList/sortTexts.poc")

    def testSortTimes(self):
        self.checkOutput("sortList/sortTimes.poc")


