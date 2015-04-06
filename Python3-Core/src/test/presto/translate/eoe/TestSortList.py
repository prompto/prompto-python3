from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestSortList(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceEOE("sortList/sortBooleans.pec")

    def testSortDates(self):
        self.compareResourceEOE("sortList/sortDates.pec")

    def testSortDateTimes(self):
        self.compareResourceEOE("sortList/sortDateTimes.pec")

    def testSortDecimals(self):
        self.compareResourceEOE("sortList/sortDecimals.pec")

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


