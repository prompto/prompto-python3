from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestSortList(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceOSO("sortList/sortBooleans.poc")

    def testSortDates(self):
        self.compareResourceOSO("sortList/sortDates.poc")

    def testSortDateTimes(self):
        self.compareResourceOSO("sortList/sortDateTimes.poc")

    def testSortDecimals(self):
        self.compareResourceOSO("sortList/sortDecimals.poc")

    def testSortExpressions(self):
        self.compareResourceOSO("sortList/sortExpressions.poc")

    def testSortIntegers(self):
        self.compareResourceOSO("sortList/sortIntegers.poc")

    def testSortKeys(self):
        self.compareResourceOSO("sortList/sortKeys.poc")

    def testSortMethods(self):
        self.compareResourceOSO("sortList/sortMethods.poc")

    def testSortNames(self):
        self.compareResourceOSO("sortList/sortNames.poc")

    def testSortTexts(self):
        self.compareResourceOSO("sortList/sortTexts.poc")

    def testSortTimes(self):
        self.compareResourceOSO("sortList/sortTimes.poc")


