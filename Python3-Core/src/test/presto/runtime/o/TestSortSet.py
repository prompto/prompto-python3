from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestSortSet(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSortBooleans(self):
        self.checkOutput("sortSet/sortBooleans.o")

    def testSortDates(self):
        self.checkOutput("sortSet/sortDates.o")

    def testSortDateTimes(self):
        self.checkOutput("sortSet/sortDateTimes.o")

    def testSortDecimals(self):
        self.checkOutput("sortSet/sortDecimals.o")

    def testSortExpressions(self):
        self.checkOutput("sortSet/sortExpressions.o")

    def testSortIntegers(self):
        self.checkOutput("sortSet/sortIntegers.o")

    def testSortKeys(self):
        self.checkOutput("sortSet/sortKeys.o")

    def testSortMethods(self):
        self.checkOutput("sortSet/sortMethods.o")

    def testSortNames(self):
        self.checkOutput("sortSet/sortNames.o")

    def testSortTexts(self):
        self.checkOutput("sortSet/sortTexts.o")

    def testSortTimes(self):
        self.checkOutput("sortSet/sortTimes.o")


