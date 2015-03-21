from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestSortSet(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceEOE("sortSet/sortBooleans.e")

    def testSortDates(self):
        self.compareResourceEOE("sortSet/sortDates.e")

    def testSortDateTimes(self):
        self.compareResourceEOE("sortSet/sortDateTimes.e")

    def testSortDecimals(self):
        self.compareResourceEOE("sortSet/sortDecimals.e")

    def testSortExpressions(self):
        self.compareResourceEOE("sortSet/sortExpressions.e")

    def testSortIntegers(self):
        self.compareResourceEOE("sortSet/sortIntegers.e")

    def testSortKeys(self):
        self.compareResourceEOE("sortSet/sortKeys.e")

    def testSortMethods(self):
        self.compareResourceEOE("sortSet/sortMethods.e")

    def testSortNames(self):
        self.compareResourceEOE("sortSet/sortNames.e")

    def testSortTexts(self):
        self.compareResourceEOE("sortSet/sortTexts.e")

    def testSortTimes(self):
        self.compareResourceEOE("sortSet/sortTimes.e")


