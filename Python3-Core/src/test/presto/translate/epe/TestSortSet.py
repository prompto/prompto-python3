from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestSortSet(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceEPE("sortSet/sortBooleans.e")

    def testSortDates(self):
        self.compareResourceEPE("sortSet/sortDates.e")

    def testSortDateTimes(self):
        self.compareResourceEPE("sortSet/sortDateTimes.e")

    def testSortDecimals(self):
        self.compareResourceEPE("sortSet/sortDecimals.e")

    def testSortExpressions(self):
        self.compareResourceEPE("sortSet/sortExpressions.e")

    def testSortIntegers(self):
        self.compareResourceEPE("sortSet/sortIntegers.e")

    def testSortKeys(self):
        self.compareResourceEPE("sortSet/sortKeys.e")

    def testSortMethods(self):
        self.compareResourceEPE("sortSet/sortMethods.e")

    def testSortNames(self):
        self.compareResourceEPE("sortSet/sortNames.e")

    def testSortTexts(self):
        self.compareResourceEPE("sortSet/sortTexts.e")

    def testSortTimes(self):
        self.compareResourceEPE("sortSet/sortTimes.e")


