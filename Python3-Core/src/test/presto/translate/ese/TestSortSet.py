from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestSortSet(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceESE("sortSet/sortBooleans.pec")

    def testSortDates(self):
        self.compareResourceESE("sortSet/sortDates.pec")

    def testSortDateTimes(self):
        self.compareResourceESE("sortSet/sortDateTimes.pec")

    def testSortDecimals(self):
        self.compareResourceESE("sortSet/sortDecimals.pec")

    def testSortExpressions(self):
        self.compareResourceESE("sortSet/sortExpressions.pec")

    def testSortIntegers(self):
        self.compareResourceESE("sortSet/sortIntegers.pec")

    def testSortKeys(self):
        self.compareResourceESE("sortSet/sortKeys.pec")

    def testSortMethods(self):
        self.compareResourceESE("sortSet/sortMethods.pec")

    def testSortNames(self):
        self.compareResourceESE("sortSet/sortNames.pec")

    def testSortTexts(self):
        self.compareResourceESE("sortSet/sortTexts.pec")

    def testSortTimes(self):
        self.compareResourceESE("sortSet/sortTimes.pec")


