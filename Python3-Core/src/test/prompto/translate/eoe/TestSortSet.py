from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSortSet(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceEOE("sortSet/sortBooleans.pec")

    def testSortDateTimes(self):
        self.compareResourceEOE("sortSet/sortDateTimes.pec")

    def testSortDates(self):
        self.compareResourceEOE("sortSet/sortDates.pec")

    def testSortDecimals(self):
        self.compareResourceEOE("sortSet/sortDecimals.pec")

    def testSortDescBooleans(self):
        self.compareResourceEOE("sortSet/sortDescBooleans.pec")

    def testSortDescDateTimes(self):
        self.compareResourceEOE("sortSet/sortDescDateTimes.pec")

    def testSortDescDates(self):
        self.compareResourceEOE("sortSet/sortDescDates.pec")

    def testSortDescDecimals(self):
        self.compareResourceEOE("sortSet/sortDescDecimals.pec")

    def testSortDescExpressions(self):
        self.compareResourceEOE("sortSet/sortDescExpressions.pec")

    def testSortDescIntegers(self):
        self.compareResourceEOE("sortSet/sortDescIntegers.pec")

    def testSortDescKeys(self):
        self.compareResourceEOE("sortSet/sortDescKeys.pec")

    def testSortDescMethods(self):
        self.compareResourceEOE("sortSet/sortDescMethods.pec")

    def testSortDescNames(self):
        self.compareResourceEOE("sortSet/sortDescNames.pec")

    def testSortDescTexts(self):
        self.compareResourceEOE("sortSet/sortDescTexts.pec")

    def testSortDescTimes(self):
        self.compareResourceEOE("sortSet/sortDescTimes.pec")

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


