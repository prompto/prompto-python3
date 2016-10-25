from prompto.parser.o.BaseOParserTest import BaseOParserTest

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

    def testSortDescBooleans(self):
        self.compareResourceOSO("sortSet/sortDescBooleans.poc")

    def testSortDescDates(self):
        self.compareResourceOSO("sortSet/sortDescDates.poc")

    def testSortDescDateTimes(self):
        self.compareResourceOSO("sortSet/sortDescDateTimes.poc")

    def testSortDescDecimals(self):
        self.compareResourceOSO("sortSet/sortDescDecimals.poc")

    def testSortDescExpressions(self):
        self.compareResourceOSO("sortSet/sortDescExpressions.poc")

    def testSortDescIntegers(self):
        self.compareResourceOSO("sortSet/sortDescIntegers.poc")

    def testSortDescKeys(self):
        self.compareResourceOSO("sortSet/sortDescKeys.poc")

    def testSortDescMethods(self):
        self.compareResourceOSO("sortSet/sortDescMethods.poc")

    def testSortDescNames(self):
        self.compareResourceOSO("sortSet/sortDescNames.poc")

    def testSortDescTexts(self):
        self.compareResourceOSO("sortSet/sortDescTexts.poc")

    def testSortDescTimes(self):
        self.compareResourceOSO("sortSet/sortDescTimes.poc")

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


