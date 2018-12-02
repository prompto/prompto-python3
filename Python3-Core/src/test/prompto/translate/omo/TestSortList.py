from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestSortList(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceOMO("sortList/sortBooleans.poc")

    def testSortDateTimes(self):
        self.compareResourceOMO("sortList/sortDateTimes.poc")

    def testSortDates(self):
        self.compareResourceOMO("sortList/sortDates.poc")

    def testSortDecimals(self):
        self.compareResourceOMO("sortList/sortDecimals.poc")

    def testSortDescBooleans(self):
        self.compareResourceOMO("sortList/sortDescBooleans.poc")

    def testSortDescDateTimes(self):
        self.compareResourceOMO("sortList/sortDescDateTimes.poc")

    def testSortDescDates(self):
        self.compareResourceOMO("sortList/sortDescDates.poc")

    def testSortDescDecimals(self):
        self.compareResourceOMO("sortList/sortDescDecimals.poc")

    def testSortDescExpressions(self):
        self.compareResourceOMO("sortList/sortDescExpressions.poc")

    def testSortDescIntegers(self):
        self.compareResourceOMO("sortList/sortDescIntegers.poc")

    def testSortDescKeys(self):
        self.compareResourceOMO("sortList/sortDescKeys.poc")

    def testSortDescMethods(self):
        self.compareResourceOMO("sortList/sortDescMethods.poc")

    def testSortDescNames(self):
        self.compareResourceOMO("sortList/sortDescNames.poc")

    def testSortDescTexts(self):
        self.compareResourceOMO("sortList/sortDescTexts.poc")

    def testSortDescTimes(self):
        self.compareResourceOMO("sortList/sortDescTimes.poc")

    def testSortDocumentExpressions(self):
        self.compareResourceOMO("sortList/sortDocumentExpressions.poc")

    def testSortDocumentKeys(self):
        self.compareResourceOMO("sortList/sortDocumentKeys.poc")

    def testSortDocumentMethods(self):
        self.compareResourceOMO("sortList/sortDocumentMethods.poc")

    def testSortDocumentNames(self):
        self.compareResourceOMO("sortList/sortDocumentNames.poc")

    def testSortExpressions(self):
        self.compareResourceOMO("sortList/sortExpressions.poc")

    def testSortIntegers(self):
        self.compareResourceOMO("sortList/sortIntegers.poc")

    def testSortKeys(self):
        self.compareResourceOMO("sortList/sortKeys.poc")

    def testSortMethods(self):
        self.compareResourceOMO("sortList/sortMethods.poc")

    def testSortNames(self):
        self.compareResourceOMO("sortList/sortNames.poc")

    def testSortTexts(self):
        self.compareResourceOMO("sortList/sortTexts.poc")

    def testSortTimes(self):
        self.compareResourceOMO("sortList/sortTimes.poc")


