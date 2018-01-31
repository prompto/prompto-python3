from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSortSet(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceEME("sortSet/sortBooleans.pec")

    def testSortDateTimes(self):
        self.compareResourceEME("sortSet/sortDateTimes.pec")

    def testSortDates(self):
        self.compareResourceEME("sortSet/sortDates.pec")

    def testSortDecimals(self):
        self.compareResourceEME("sortSet/sortDecimals.pec")

    def testSortDescBooleans(self):
        self.compareResourceEME("sortSet/sortDescBooleans.pec")

    def testSortDescDateTimes(self):
        self.compareResourceEME("sortSet/sortDescDateTimes.pec")

    def testSortDescDates(self):
        self.compareResourceEME("sortSet/sortDescDates.pec")

    def testSortDescDecimals(self):
        self.compareResourceEME("sortSet/sortDescDecimals.pec")

    def testSortDescExpressions(self):
        self.compareResourceEME("sortSet/sortDescExpressions.pec")

    def testSortDescIntegers(self):
        self.compareResourceEME("sortSet/sortDescIntegers.pec")

    def testSortDescKeys(self):
        self.compareResourceEME("sortSet/sortDescKeys.pec")

    def testSortDescMethods(self):
        self.compareResourceEME("sortSet/sortDescMethods.pec")

    def testSortDescNames(self):
        self.compareResourceEME("sortSet/sortDescNames.pec")

    def testSortDescTexts(self):
        self.compareResourceEME("sortSet/sortDescTexts.pec")

    def testSortDescTimes(self):
        self.compareResourceEME("sortSet/sortDescTimes.pec")

    def testSortExpressions(self):
        self.compareResourceEME("sortSet/sortExpressions.pec")

    def testSortIntegers(self):
        self.compareResourceEME("sortSet/sortIntegers.pec")

    def testSortKeys(self):
        self.compareResourceEME("sortSet/sortKeys.pec")

    def testSortMethods(self):
        self.compareResourceEME("sortSet/sortMethods.pec")

    def testSortNames(self):
        self.compareResourceEME("sortSet/sortNames.pec")

    def testSortTexts(self):
        self.compareResourceEME("sortSet/sortTexts.pec")

    def testSortTimes(self):
        self.compareResourceEME("sortSet/sortTimes.pec")


