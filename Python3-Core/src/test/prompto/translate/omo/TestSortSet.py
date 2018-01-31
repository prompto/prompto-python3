from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestSortSet(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceOMO("sortSet/sortBooleans.poc")

    def testSortDateTimes(self):
        self.compareResourceOMO("sortSet/sortDateTimes.poc")

    def testSortDates(self):
        self.compareResourceOMO("sortSet/sortDates.poc")

    def testSortDecimals(self):
        self.compareResourceOMO("sortSet/sortDecimals.poc")

    def testSortDescBooleans(self):
        self.compareResourceOMO("sortSet/sortDescBooleans.poc")

    def testSortDescDateTimes(self):
        self.compareResourceOMO("sortSet/sortDescDateTimes.poc")

    def testSortDescDates(self):
        self.compareResourceOMO("sortSet/sortDescDates.poc")

    def testSortDescDecimals(self):
        self.compareResourceOMO("sortSet/sortDescDecimals.poc")

    def testSortDescExpressions(self):
        self.compareResourceOMO("sortSet/sortDescExpressions.poc")

    def testSortDescIntegers(self):
        self.compareResourceOMO("sortSet/sortDescIntegers.poc")

    def testSortDescKeys(self):
        self.compareResourceOMO("sortSet/sortDescKeys.poc")

    def testSortDescMethods(self):
        self.compareResourceOMO("sortSet/sortDescMethods.poc")

    def testSortDescNames(self):
        self.compareResourceOMO("sortSet/sortDescNames.poc")

    def testSortDescTexts(self):
        self.compareResourceOMO("sortSet/sortDescTexts.poc")

    def testSortDescTimes(self):
        self.compareResourceOMO("sortSet/sortDescTimes.poc")

    def testSortExpressions(self):
        self.compareResourceOMO("sortSet/sortExpressions.poc")

    def testSortIntegers(self):
        self.compareResourceOMO("sortSet/sortIntegers.poc")

    def testSortKeys(self):
        self.compareResourceOMO("sortSet/sortKeys.poc")

    def testSortMethods(self):
        self.compareResourceOMO("sortSet/sortMethods.poc")

    def testSortNames(self):
        self.compareResourceOMO("sortSet/sortNames.poc")

    def testSortTexts(self):
        self.compareResourceOMO("sortSet/sortTexts.poc")

    def testSortTimes(self):
        self.compareResourceOMO("sortSet/sortTimes.poc")


