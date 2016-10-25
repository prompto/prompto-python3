from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestSortList(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceOEO("sortList/sortBooleans.poc")

    def testSortDates(self):
        self.compareResourceOEO("sortList/sortDates.poc")

    def testSortDateTimes(self):
        self.compareResourceOEO("sortList/sortDateTimes.poc")

    def testSortDecimals(self):
        self.compareResourceOEO("sortList/sortDecimals.poc")

    def testSortDescBooleans(self):
        self.compareResourceOEO("sortList/sortDescBooleans.poc")

    def testSortDescDates(self):
        self.compareResourceOEO("sortList/sortDescDates.poc")

    def testSortDescDateTimes(self):
        self.compareResourceOEO("sortList/sortDescDateTimes.poc")

    def testSortDescDecimals(self):
        self.compareResourceOEO("sortList/sortDescDecimals.poc")

    def testSortDescExpressions(self):
        self.compareResourceOEO("sortList/sortDescExpressions.poc")

    def testSortDescIntegers(self):
        self.compareResourceOEO("sortList/sortDescIntegers.poc")

    def testSortDescKeys(self):
        self.compareResourceOEO("sortList/sortDescKeys.poc")

    def testSortDescMethods(self):
        self.compareResourceOEO("sortList/sortDescMethods.poc")

    def testSortDescNames(self):
        self.compareResourceOEO("sortList/sortDescNames.poc")

    def testSortDescTexts(self):
        self.compareResourceOEO("sortList/sortDescTexts.poc")

    def testSortDescTimes(self):
        self.compareResourceOEO("sortList/sortDescTimes.poc")

    def testSortExpressions(self):
        self.compareResourceOEO("sortList/sortExpressions.poc")

    def testSortIntegers(self):
        self.compareResourceOEO("sortList/sortIntegers.poc")

    def testSortKeys(self):
        self.compareResourceOEO("sortList/sortKeys.poc")

    def testSortMethods(self):
        self.compareResourceOEO("sortList/sortMethods.poc")

    def testSortNames(self):
        self.compareResourceOEO("sortList/sortNames.poc")

    def testSortTexts(self):
        self.compareResourceOEO("sortList/sortTexts.poc")

    def testSortTimes(self):
        self.compareResourceOEO("sortList/sortTimes.poc")


