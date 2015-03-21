from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestSortSet(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceOEO("sortSet/sortBooleans.o")

    def testSortDates(self):
        self.compareResourceOEO("sortSet/sortDates.o")

    def testSortDateTimes(self):
        self.compareResourceOEO("sortSet/sortDateTimes.o")

    def testSortDecimals(self):
        self.compareResourceOEO("sortSet/sortDecimals.o")

    def testSortExpressions(self):
        self.compareResourceOEO("sortSet/sortExpressions.o")

    def testSortIntegers(self):
        self.compareResourceOEO("sortSet/sortIntegers.o")

    def testSortKeys(self):
        self.compareResourceOEO("sortSet/sortKeys.o")

    def testSortMethods(self):
        self.compareResourceOEO("sortSet/sortMethods.o")

    def testSortNames(self):
        self.compareResourceOEO("sortSet/sortNames.o")

    def testSortTexts(self):
        self.compareResourceOEO("sortSet/sortTexts.o")

    def testSortTimes(self):
        self.compareResourceOEO("sortSet/sortTimes.o")


