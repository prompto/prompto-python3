from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSortList(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceEOE("sortList/sortBooleans.pec")

    def testSortDateTimes(self):
        self.compareResourceEOE("sortList/sortDateTimes.pec")

    def testSortDates(self):
        self.compareResourceEOE("sortList/sortDates.pec")

    def testSortDecimals(self):
        self.compareResourceEOE("sortList/sortDecimals.pec")

    def testSortDescBooleans(self):
        self.compareResourceEOE("sortList/sortDescBooleans.pec")

    def testSortDescDateTimes(self):
        self.compareResourceEOE("sortList/sortDescDateTimes.pec")

    def testSortDescDates(self):
        self.compareResourceEOE("sortList/sortDescDates.pec")

    def testSortDescDecimals(self):
        self.compareResourceEOE("sortList/sortDescDecimals.pec")

    def testSortDescExpressions(self):
        self.compareResourceEOE("sortList/sortDescExpressions.pec")

    def testSortDescIntegers(self):
        self.compareResourceEOE("sortList/sortDescIntegers.pec")

    def testSortDescKeys(self):
        self.compareResourceEOE("sortList/sortDescKeys.pec")

    def testSortDescMethods(self):
        self.compareResourceEOE("sortList/sortDescMethods.pec")

    def testSortDescNames(self):
        self.compareResourceEOE("sortList/sortDescNames.pec")

    def testSortDescTexts(self):
        self.compareResourceEOE("sortList/sortDescTexts.pec")

    def testSortDescTimes(self):
        self.compareResourceEOE("sortList/sortDescTimes.pec")

    def testSortExpressions(self):
        self.compareResourceEOE("sortList/sortExpressions.pec")

    def testSortIntegers(self):
        self.compareResourceEOE("sortList/sortIntegers.pec")

    def testSortKeys(self):
        self.compareResourceEOE("sortList/sortKeys.pec")

    def testSortMethods(self):
        self.compareResourceEOE("sortList/sortMethods.pec")

    def testSortNames(self):
        self.compareResourceEOE("sortList/sortNames.pec")

    def testSortTexts(self):
        self.compareResourceEOE("sortList/sortTexts.pec")

    def testSortTimes(self):
        self.compareResourceEOE("sortList/sortTimes.pec")


