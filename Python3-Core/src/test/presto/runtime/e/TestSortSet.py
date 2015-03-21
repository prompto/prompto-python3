from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestSortSet(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSortBooleans(self):
        self.checkOutput("sortSet/sortBooleans.e")

    def testSortDates(self):
        self.checkOutput("sortSet/sortDates.e")

    def testSortDateTimes(self):
        self.checkOutput("sortSet/sortDateTimes.e")

    def testSortDecimals(self):
        self.checkOutput("sortSet/sortDecimals.e")

    def testSortExpressions(self):
        self.checkOutput("sortSet/sortExpressions.e")

    def testSortIntegers(self):
        self.checkOutput("sortSet/sortIntegers.e")

    def testSortKeys(self):
        self.checkOutput("sortSet/sortKeys.e")

    def testSortMethods(self):
        self.checkOutput("sortSet/sortMethods.e")

    def testSortNames(self):
        self.checkOutput("sortSet/sortNames.e")

    def testSortTexts(self):
        self.checkOutput("sortSet/sortTexts.e")

    def testSortTimes(self):
        self.checkOutput("sortSet/sortTimes.e")


