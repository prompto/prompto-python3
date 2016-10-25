from prompto.parser.e.BaseEParserTest import BaseEParserTest

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

    def testSortDescBooleans(self):
        self.compareResourceESE("sortSet/sortDescBooleans.pec")

    def testSortDescDates(self):
        self.compareResourceESE("sortSet/sortDescDates.pec")

    def testSortDescDateTimes(self):
        self.compareResourceESE("sortSet/sortDescDateTimes.pec")

    def testSortDescDecimals(self):
        self.compareResourceESE("sortSet/sortDescDecimals.pec")

    def testSortDescExpressions(self):
        self.compareResourceESE("sortSet/sortDescExpressions.pec")

    def testSortDescIntegers(self):
        self.compareResourceESE("sortSet/sortDescIntegers.pec")

    def testSortDescKeys(self):
        self.compareResourceESE("sortSet/sortDescKeys.pec")

    def testSortDescMethods(self):
        self.compareResourceESE("sortSet/sortDescMethods.pec")

    def testSortDescNames(self):
        self.compareResourceESE("sortSet/sortDescNames.pec")

    def testSortDescTexts(self):
        self.compareResourceESE("sortSet/sortDescTexts.pec")

    def testSortDescTimes(self):
        self.compareResourceESE("sortSet/sortDescTimes.pec")

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


