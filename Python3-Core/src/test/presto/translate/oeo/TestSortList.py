from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestSortList(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceOEO("sortList/sortBooleans.o")

    def testSortDates(self):
        self.compareResourceOEO("sortList/sortDates.o")

    def testSortDateTimes(self):
        self.compareResourceOEO("sortList/sortDateTimes.o")

    def testSortDecimals(self):
        self.compareResourceOEO("sortList/sortDecimals.o")

    def testSortExpressions(self):
        self.compareResourceOEO("sortList/sortExpressions.o")

    def testSortIntegers(self):
        self.compareResourceOEO("sortList/sortIntegers.o")

    def testSortKeys(self):
        self.compareResourceOEO("sortList/sortKeys.o")

    def testSortMethods(self):
        self.compareResourceOEO("sortList/sortMethods.o")

    def testSortNames(self):
        self.compareResourceOEO("sortList/sortNames.o")

    def testSortTexts(self):
        self.compareResourceOEO("sortList/sortTexts.o")

    def testSortTimes(self):
        self.compareResourceOEO("sortList/sortTimes.o")


