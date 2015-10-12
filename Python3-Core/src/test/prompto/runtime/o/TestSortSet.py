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

    def testSortDates(self):
        self.checkOutput("sortSet/sortDates.poc")

    def testSortDateTimes(self):
        self.checkOutput("sortSet/sortDateTimes.poc")

    def testSortDecimals(self):
        self.checkOutput("sortSet/sortDecimals.poc")

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


