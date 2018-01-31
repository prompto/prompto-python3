from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestSortSet(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSortBooleans(self):
        self.checkOutput("sortSet/sortBooleans.poc")

    def testSortDateTimes(self):
        self.checkOutput("sortSet/sortDateTimes.poc")

    def testSortDates(self):
        self.checkOutput("sortSet/sortDates.poc")

    def testSortDecimals(self):
        self.checkOutput("sortSet/sortDecimals.poc")

    def testSortDescBooleans(self):
        self.checkOutput("sortSet/sortDescBooleans.poc")

    def testSortDescDateTimes(self):
        self.checkOutput("sortSet/sortDescDateTimes.poc")

    def testSortDescDates(self):
        self.checkOutput("sortSet/sortDescDates.poc")

    def testSortDescDecimals(self):
        self.checkOutput("sortSet/sortDescDecimals.poc")

    def testSortDescExpressions(self):
        self.checkOutput("sortSet/sortDescExpressions.poc")

    def testSortDescIntegers(self):
        self.checkOutput("sortSet/sortDescIntegers.poc")

    def testSortDescKeys(self):
        self.checkOutput("sortSet/sortDescKeys.poc")

    def testSortDescMethods(self):
        self.checkOutput("sortSet/sortDescMethods.poc")

    def testSortDescNames(self):
        self.checkOutput("sortSet/sortDescNames.poc")

    def testSortDescTexts(self):
        self.checkOutput("sortSet/sortDescTexts.poc")

    def testSortDescTimes(self):
        self.checkOutput("sortSet/sortDescTimes.poc")

    def testSortExpressions(self):
        self.checkOutput("sortSet/sortExpressions.poc")

    def testSortIntegers(self):
        self.checkOutput("sortSet/sortIntegers.poc")

    def testSortKeys(self):
        self.checkOutput("sortSet/sortKeys.poc")

    def testSortMethods(self):
        self.checkOutput("sortSet/sortMethods.poc")

    def testSortNames(self):
        self.checkOutput("sortSet/sortNames.poc")

    def testSortTexts(self):
        self.checkOutput("sortSet/sortTexts.poc")

    def testSortTimes(self):
        self.checkOutput("sortSet/sortTimes.poc")


