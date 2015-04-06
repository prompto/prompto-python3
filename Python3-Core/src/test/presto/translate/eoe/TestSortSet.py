from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestSortSet(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceEOE("sortSet/sortBooleans.pec")

    def testSortDates(self):
        self.compareResourceEOE("sortSet/sortDates.pec")

    def testSortDateTimes(self):
        self.compareResourceEOE("sortSet/sortDateTimes.pec")

    def testSortDecimals(self):
        self.compareResourceEOE("sortSet/sortDecimals.pec")

    def testSortExpressions(self):
        self.compareResourceEOE("sortSet/sortExpressions.pec")

    def testSortIntegers(self):
        self.compareResourceEOE("sortSet/sortIntegers.pec")

    def testSortKeys(self):
        self.compareResourceEOE("sortSet/sortKeys.pec")

    def testSortMethods(self):
        self.compareResourceEOE("sortSet/sortMethods.pec")

    def testSortNames(self):
        self.compareResourceEOE("sortSet/sortNames.pec")

    def testSortTexts(self):
        self.compareResourceEOE("sortSet/sortTexts.pec")

    def testSortTimes(self):
        self.compareResourceEOE("sortSet/sortTimes.pec")


