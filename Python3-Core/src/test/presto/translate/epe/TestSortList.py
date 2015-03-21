from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestSortList(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceEPE("sortList/sortBooleans.e")

    def testSortDates(self):
        self.compareResourceEPE("sortList/sortDates.e")

    def testSortDateTimes(self):
        self.compareResourceEPE("sortList/sortDateTimes.e")

    def testSortDecimals(self):
        self.compareResourceEPE("sortList/sortDecimals.e")

    def testSortExpressions(self):
        self.compareResourceEPE("sortList/sortExpressions.e")

    def testSortIntegers(self):
        self.compareResourceEPE("sortList/sortIntegers.e")

    def testSortKeys(self):
        self.compareResourceEPE("sortList/sortKeys.e")

    def testSortMethods(self):
        self.compareResourceEPE("sortList/sortMethods.e")

    def testSortNames(self):
        self.compareResourceEPE("sortList/sortNames.e")

    def testSortTexts(self):
        self.compareResourceEPE("sortList/sortTexts.e")

    def testSortTimes(self):
        self.compareResourceEPE("sortList/sortTimes.e")


