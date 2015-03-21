from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestSortList(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceEOE("sortList/sortBooleans.e")

    def testSortDates(self):
        self.compareResourceEOE("sortList/sortDates.e")

    def testSortDateTimes(self):
        self.compareResourceEOE("sortList/sortDateTimes.e")

    def testSortDecimals(self):
        self.compareResourceEOE("sortList/sortDecimals.e")

    def testSortExpressions(self):
        self.compareResourceEOE("sortList/sortExpressions.e")

    def testSortIntegers(self):
        self.compareResourceEOE("sortList/sortIntegers.e")

    def testSortKeys(self):
        self.compareResourceEOE("sortList/sortKeys.e")

    def testSortMethods(self):
        self.compareResourceEOE("sortList/sortMethods.e")

    def testSortNames(self):
        self.compareResourceEOE("sortList/sortNames.e")

    def testSortTexts(self):
        self.compareResourceEOE("sortList/sortTexts.e")

    def testSortTimes(self):
        self.compareResourceEOE("sortList/sortTimes.e")


