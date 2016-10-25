from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestSortSet(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSortBooleans(self):
        self.checkOutput("sortSet/sortBooleans.pec")

    def testSortDates(self):
        self.checkOutput("sortSet/sortDates.pec")

    def testSortDateTimes(self):
        self.checkOutput("sortSet/sortDateTimes.pec")

    def testSortDecimals(self):
        self.checkOutput("sortSet/sortDecimals.pec")

    def testSortDescBooleans(self):
        self.checkOutput("sortSet/sortDescBooleans.pec")

    def testSortDescDates(self):
        self.checkOutput("sortSet/sortDescDates.pec")

    def testSortDescDateTimes(self):
        self.checkOutput("sortSet/sortDescDateTimes.pec")

    def testSortDescDecimals(self):
        self.checkOutput("sortSet/sortDescDecimals.pec")

    def testSortDescExpressions(self):
        self.checkOutput("sortSet/sortDescExpressions.pec")

    def testSortDescIntegers(self):
        self.checkOutput("sortSet/sortDescIntegers.pec")

    def testSortDescKeys(self):
        self.checkOutput("sortSet/sortDescKeys.pec")

    def testSortDescMethods(self):
        self.checkOutput("sortSet/sortDescMethods.pec")

    def testSortDescNames(self):
        self.checkOutput("sortSet/sortDescNames.pec")

    def testSortDescTexts(self):
        self.checkOutput("sortSet/sortDescTexts.pec")

    def testSortDescTimes(self):
        self.checkOutput("sortSet/sortDescTimes.pec")

    def testSortExpressions(self):
        self.checkOutput("sortSet/sortExpressions.pec")

    def testSortIntegers(self):
        self.checkOutput("sortSet/sortIntegers.pec")

    def testSortKeys(self):
        self.checkOutput("sortSet/sortKeys.pec")

    def testSortMethods(self):
        self.checkOutput("sortSet/sortMethods.pec")

    def testSortNames(self):
        self.checkOutput("sortSet/sortNames.pec")

    def testSortTexts(self):
        self.checkOutput("sortSet/sortTexts.pec")

    def testSortTimes(self):
        self.checkOutput("sortSet/sortTimes.pec")


