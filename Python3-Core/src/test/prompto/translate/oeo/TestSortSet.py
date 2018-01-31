from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestSortSet(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceOEO("sortSet/sortBooleans.poc")

    def testSortDateTimes(self):
        self.compareResourceOEO("sortSet/sortDateTimes.poc")

    def testSortDates(self):
        self.compareResourceOEO("sortSet/sortDates.poc")

    def testSortDecimals(self):
        self.compareResourceOEO("sortSet/sortDecimals.poc")

    def testSortDescBooleans(self):
        self.compareResourceOEO("sortSet/sortDescBooleans.poc")

    def testSortDescDateTimes(self):
        self.compareResourceOEO("sortSet/sortDescDateTimes.poc")

    def testSortDescDates(self):
        self.compareResourceOEO("sortSet/sortDescDates.poc")

    def testSortDescDecimals(self):
        self.compareResourceOEO("sortSet/sortDescDecimals.poc")

    def testSortDescExpressions(self):
        self.compareResourceOEO("sortSet/sortDescExpressions.poc")

    def testSortDescIntegers(self):
        self.compareResourceOEO("sortSet/sortDescIntegers.poc")

    def testSortDescKeys(self):
        self.compareResourceOEO("sortSet/sortDescKeys.poc")

    def testSortDescMethods(self):
        self.compareResourceOEO("sortSet/sortDescMethods.poc")

    def testSortDescNames(self):
        self.compareResourceOEO("sortSet/sortDescNames.poc")

    def testSortDescTexts(self):
        self.compareResourceOEO("sortSet/sortDescTexts.poc")

    def testSortDescTimes(self):
        self.compareResourceOEO("sortSet/sortDescTimes.poc")

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


