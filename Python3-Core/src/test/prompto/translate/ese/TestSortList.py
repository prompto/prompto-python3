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


