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


