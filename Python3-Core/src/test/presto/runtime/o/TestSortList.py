from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestSortList(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSortBooleans(self):
        self.checkOutput("sortList/sortBooleans.o")

    def testSortDates(self):
        self.checkOutput("sortList/sortDates.o")

    def testSortDateTimes(self):
        self.checkOutput("sortList/sortDateTimes.o")

    def testSortDecimals(self):
        self.checkOutput("sortList/sortDecimals.o")

    def testSortExpressions(self):
        self.checkOutput("sortList/sortExpressions.o")

    def testSortIntegers(self):
        self.checkOutput("sortList/sortIntegers.o")

    def testSortKeys(self):
        self.checkOutput("sortList/sortKeys.o")

    def testSortMethods(self):
        self.checkOutput("sortList/sortMethods.o")

    def testSortNames(self):
        self.checkOutput("sortList/sortNames.o")

    def testSortTexts(self):
        self.checkOutput("sortList/sortTexts.o")

    def testSortTimes(self):
        self.checkOutput("sortList/sortTimes.o")


