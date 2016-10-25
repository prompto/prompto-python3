from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSortList(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceESE("sortList/sortBooleans.pec")

    def testSortDates(self):
        self.compareResourceESE("sortList/sortDates.pec")

    def testSortDateTimes(self):
        self.compareResourceESE("sortList/sortDateTimes.pec")

    def testSortDecimals(self):
        self.compareResourceESE("sortList/sortDecimals.pec")

    def testSortDescBooleans(self):
        self.compareResourceESE("sortList/sortDescBooleans.pec")

    def testSortDescDates(self):
        self.compareResourceESE("sortList/sortDescDates.pec")

    def testSortDescDateTimes(self):
        self.compareResourceESE("sortList/sortDescDateTimes.pec")

    def testSortDescDecimals(self):
        self.compareResourceESE("sortList/sortDescDecimals.pec")

    def testSortDescExpressions(self):
        self.compareResourceESE("sortList/sortDescExpressions.pec")

    def testSortDescIntegers(self):
        self.compareResourceESE("sortList/sortDescIntegers.pec")

    def testSortDescKeys(self):
        self.compareResourceESE("sortList/sortDescKeys.pec")

    def testSortDescMethods(self):
        self.compareResourceESE("sortList/sortDescMethods.pec")

    def testSortDescNames(self):
        self.compareResourceESE("sortList/sortDescNames.pec")

    def testSortDescTexts(self):
        self.compareResourceESE("sortList/sortDescTexts.pec")

    def testSortDescTimes(self):
        self.compareResourceESE("sortList/sortDescTimes.pec")

    def testSortExpressions(self):
        self.compareResourceESE("sortList/sortExpressions.pec")

    def testSortIntegers(self):
        self.compareResourceESE("sortList/sortIntegers.pec")

    def testSortKeys(self):
        self.compareResourceESE("sortList/sortKeys.pec")

    def testSortMethods(self):
        self.compareResourceESE("sortList/sortMethods.pec")

    def testSortNames(self):
        self.compareResourceESE("sortList/sortNames.pec")

    def testSortTexts(self):
        self.compareResourceESE("sortList/sortTexts.pec")

    def testSortTimes(self):
        self.compareResourceESE("sortList/sortTimes.pec")


