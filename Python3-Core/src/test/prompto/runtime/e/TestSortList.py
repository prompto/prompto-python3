from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestSortList(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSortBooleans(self):
        self.checkOutput("sortList/sortBooleans.pec")

    def testSortDates(self):
        self.checkOutput("sortList/sortDates.pec")

    def testSortDateTimes(self):
        self.checkOutput("sortList/sortDateTimes.pec")

    def testSortDecimals(self):
        self.checkOutput("sortList/sortDecimals.pec")

    def testSortDescBooleans(self):
        self.checkOutput("sortList/sortDescBooleans.pec")

    def testSortDescDates(self):
        self.checkOutput("sortList/sortDescDates.pec")

    def testSortDescDateTimes(self):
        self.checkOutput("sortList/sortDescDateTimes.pec")

    def testSortDescDecimals(self):
        self.checkOutput("sortList/sortDescDecimals.pec")

    def testSortDescExpressions(self):
        self.checkOutput("sortList/sortDescExpressions.pec")

    def testSortDescIntegers(self):
        self.checkOutput("sortList/sortDescIntegers.pec")

    def testSortDescKeys(self):
        self.checkOutput("sortList/sortDescKeys.pec")

    def testSortDescMethods(self):
        self.checkOutput("sortList/sortDescMethods.pec")

    def testSortDescNames(self):
        self.checkOutput("sortList/sortDescNames.pec")

    def testSortDescTexts(self):
        self.checkOutput("sortList/sortDescTexts.pec")

    def testSortDescTimes(self):
        self.checkOutput("sortList/sortDescTimes.pec")

    def testSortExpressions(self):
        self.checkOutput("sortList/sortExpressions.pec")

    def testSortIntegers(self):
        self.checkOutput("sortList/sortIntegers.pec")

    def testSortKeys(self):
        self.checkOutput("sortList/sortKeys.pec")

    def testSortMethods(self):
        self.checkOutput("sortList/sortMethods.pec")

    def testSortNames(self):
        self.checkOutput("sortList/sortNames.pec")

    def testSortTexts(self):
        self.checkOutput("sortList/sortTexts.pec")

    def testSortTimes(self):
        self.checkOutput("sortList/sortTimes.pec")


