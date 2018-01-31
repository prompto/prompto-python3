from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestSortList(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSortBooleans(self):
        self.checkOutput("sortList/sortBooleans.poc")

    def testSortDateTimes(self):
        self.checkOutput("sortList/sortDateTimes.poc")

    def testSortDates(self):
        self.checkOutput("sortList/sortDates.poc")

    def testSortDecimals(self):
        self.checkOutput("sortList/sortDecimals.poc")

    def testSortDescBooleans(self):
        self.checkOutput("sortList/sortDescBooleans.poc")

    def testSortDescDateTimes(self):
        self.checkOutput("sortList/sortDescDateTimes.poc")

    def testSortDescDates(self):
        self.checkOutput("sortList/sortDescDates.poc")

    def testSortDescDecimals(self):
        self.checkOutput("sortList/sortDescDecimals.poc")

    def testSortDescExpressions(self):
        self.checkOutput("sortList/sortDescExpressions.poc")

    def testSortDescIntegers(self):
        self.checkOutput("sortList/sortDescIntegers.poc")

    def testSortDescKeys(self):
        self.checkOutput("sortList/sortDescKeys.poc")

    def testSortDescMethods(self):
        self.checkOutput("sortList/sortDescMethods.poc")

    def testSortDescNames(self):
        self.checkOutput("sortList/sortDescNames.poc")

    def testSortDescTexts(self):
        self.checkOutput("sortList/sortDescTexts.poc")

    def testSortDescTimes(self):
        self.checkOutput("sortList/sortDescTimes.poc")

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


