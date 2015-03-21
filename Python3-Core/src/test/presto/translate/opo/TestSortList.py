from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestSortList(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceOPO("sortList/sortBooleans.o")

    def testSortDates(self):
        self.compareResourceOPO("sortList/sortDates.o")

    def testSortDateTimes(self):
        self.compareResourceOPO("sortList/sortDateTimes.o")

    def testSortDecimals(self):
        self.compareResourceOPO("sortList/sortDecimals.o")

    def testSortExpressions(self):
        self.compareResourceOPO("sortList/sortExpressions.o")

    def testSortIntegers(self):
        self.compareResourceOPO("sortList/sortIntegers.o")

    def testSortKeys(self):
        self.compareResourceOPO("sortList/sortKeys.o")

    def testSortMethods(self):
        self.compareResourceOPO("sortList/sortMethods.o")

    def testSortNames(self):
        self.compareResourceOPO("sortList/sortNames.o")

    def testSortTexts(self):
        self.compareResourceOPO("sortList/sortTexts.o")

    def testSortTimes(self):
        self.compareResourceOPO("sortList/sortTimes.o")


