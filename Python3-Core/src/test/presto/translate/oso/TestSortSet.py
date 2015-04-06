from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestSortSet(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceOSO("sortSet/sortBooleans.poc")

    def testSortDates(self):
        self.compareResourceOSO("sortSet/sortDates.poc")

    def testSortDateTimes(self):
        self.compareResourceOSO("sortSet/sortDateTimes.poc")

    def testSortDecimals(self):
        self.compareResourceOSO("sortSet/sortDecimals.poc")

    def testSortExpressions(self):
        self.compareResourceOSO("sortSet/sortExpressions.poc")

    def testSortIntegers(self):
        self.compareResourceOSO("sortSet/sortIntegers.poc")

    def testSortKeys(self):
        self.compareResourceOSO("sortSet/sortKeys.poc")

    def testSortMethods(self):
        self.compareResourceOSO("sortSet/sortMethods.poc")

    def testSortNames(self):
        self.compareResourceOSO("sortSet/sortNames.poc")

    def testSortTexts(self):
        self.compareResourceOSO("sortSet/sortTexts.poc")

    def testSortTimes(self):
        self.compareResourceOSO("sortSet/sortTimes.poc")


