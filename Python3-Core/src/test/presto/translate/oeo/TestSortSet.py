from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestSortSet(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceOEO("sortSet/sortBooleans.poc")

    def testSortDates(self):
        self.compareResourceOEO("sortSet/sortDates.poc")

    def testSortDateTimes(self):
        self.compareResourceOEO("sortSet/sortDateTimes.poc")

    def testSortDecimals(self):
        self.compareResourceOEO("sortSet/sortDecimals.poc")

    def testSortExpressions(self):
        self.compareResourceOEO("sortSet/sortExpressions.poc")

    def testSortIntegers(self):
        self.compareResourceOEO("sortSet/sortIntegers.poc")

    def testSortKeys(self):
        self.compareResourceOEO("sortSet/sortKeys.poc")

    def testSortMethods(self):
        self.compareResourceOEO("sortSet/sortMethods.poc")

    def testSortNames(self):
        self.compareResourceOEO("sortSet/sortNames.poc")

    def testSortTexts(self):
        self.compareResourceOEO("sortSet/sortTexts.poc")

    def testSortTimes(self):
        self.compareResourceOEO("sortSet/sortTimes.poc")


