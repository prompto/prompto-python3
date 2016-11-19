from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSortList(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSortBooleans(self):
        self.compareResourceEME("sortList/sortBooleans.pec")

    def testSortDates(self):
        self.compareResourceEME("sortList/sortDates.pec")

    def testSortDateTimes(self):
        self.compareResourceEME("sortList/sortDateTimes.pec")

    def testSortDecimals(self):
        self.compareResourceEME("sortList/sortDecimals.pec")

    def testSortDescBooleans(self):
        self.compareResourceEME("sortList/sortDescBooleans.pec")

    def testSortDescDates(self):
        self.compareResourceEME("sortList/sortDescDates.pec")

    def testSortDescDateTimes(self):
        self.compareResourceEME("sortList/sortDescDateTimes.pec")

    def testSortDescDecimals(self):
        self.compareResourceEME("sortList/sortDescDecimals.pec")

    def testSortDescExpressions(self):
        self.compareResourceEME("sortList/sortDescExpressions.pec")

    def testSortDescIntegers(self):
        self.compareResourceEME("sortList/sortDescIntegers.pec")

    def testSortDescKeys(self):
        self.compareResourceEME("sortList/sortDescKeys.pec")

    def testSortDescMethods(self):
        self.compareResourceEME("sortList/sortDescMethods.pec")

    def testSortDescNames(self):
        self.compareResourceEME("sortList/sortDescNames.pec")

    def testSortDescTexts(self):
        self.compareResourceEME("sortList/sortDescTexts.pec")

    def testSortDescTimes(self):
        self.compareResourceEME("sortList/sortDescTimes.pec")

    def testSortExpressions(self):
        self.compareResourceEME("sortList/sortExpressions.pec")

    def testSortIntegers(self):
        self.compareResourceEME("sortList/sortIntegers.pec")

    def testSortKeys(self):
        self.compareResourceEME("sortList/sortKeys.pec")

    def testSortMethods(self):
        self.compareResourceEME("sortList/sortMethods.pec")

    def testSortNames(self):
        self.compareResourceEME("sortList/sortNames.pec")

    def testSortTexts(self):
        self.compareResourceEME("sortList/sortTexts.pec")

    def testSortTimes(self):
        self.compareResourceEME("sortList/sortTimes.pec")


