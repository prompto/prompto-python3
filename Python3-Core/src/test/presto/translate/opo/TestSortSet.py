from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestSortSet(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceOPO("sortSet/sortBooleans.o")

    def testSortDates(self):
        self.compareResourceOPO("sortSet/sortDates.o")

    def testSortDateTimes(self):
        self.compareResourceOPO("sortSet/sortDateTimes.o")

    def testSortDecimals(self):
        self.compareResourceOPO("sortSet/sortDecimals.o")

    def testSortExpressions(self):
        self.compareResourceOPO("sortSet/sortExpressions.o")

    def testSortIntegers(self):
        self.compareResourceOPO("sortSet/sortIntegers.o")

    def testSortKeys(self):
        self.compareResourceOPO("sortSet/sortKeys.o")

    def testSortMethods(self):
        self.compareResourceOPO("sortSet/sortMethods.o")

    def testSortNames(self):
        self.compareResourceOPO("sortSet/sortNames.o")

    def testSortTexts(self):
        self.compareResourceOPO("sortSet/sortTexts.o")

    def testSortTimes(self):
        self.compareResourceOPO("sortSet/sortTimes.o")


