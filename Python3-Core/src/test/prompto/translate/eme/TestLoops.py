from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestLoops(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDoWhile(self):
        self.compareResourceEME("loops/doWhile.pec")

    def testDoWhileBreak(self):
        self.compareResourceEME("loops/doWhileBreak.pec")

    def testEmbeddedForEach(self):
        self.compareResourceEME("loops/embeddedForEach.pec")

    def testForEachBreak(self):
        self.compareResourceEME("loops/forEachBreak.pec")

    def testForEachCharacterRange(self):
        self.compareResourceEME("loops/forEachCharacterRange.pec")

    def testForEachCharacterRangeWithIndex(self):
        self.compareResourceEME("loops/forEachCharacterRangeWithIndex.pec")

    def testForEachDateRange(self):
        self.compareResourceEME("loops/forEachDateRange.pec")

    def testForEachDateRangeWithIndex(self):
        self.compareResourceEME("loops/forEachDateRangeWithIndex.pec")

    def testForEachDictionaryItem(self):
        self.compareResourceEME("loops/forEachDictionaryItem.pec")

    def testForEachDictionaryItemWithIndex(self):
        self.compareResourceEME("loops/forEachDictionaryItemWithIndex.pec")

    def testForEachDictionaryKey(self):
        self.compareResourceEME("loops/forEachDictionaryKey.pec")

    def testForEachDictionaryKeyWithIndex(self):
        self.compareResourceEME("loops/forEachDictionaryKeyWithIndex.pec")

    def testForEachDictionaryValue(self):
        self.compareResourceEME("loops/forEachDictionaryValue.pec")

    def testForEachDictionaryValueWithIndex(self):
        self.compareResourceEME("loops/forEachDictionaryValueWithIndex.pec")

    def testForEachInstanceList(self):
        self.compareResourceEME("loops/forEachInstanceList.pec")

    def testForEachInstanceListWithIndex(self):
        self.compareResourceEME("loops/forEachInstanceListWithIndex.pec")

    def testForEachInstanceSet(self):
        self.compareResourceEME("loops/forEachInstanceSet.pec")

    def testForEachInstanceSetWithIndex(self):
        self.compareResourceEME("loops/forEachInstanceSetWithIndex.pec")

    def testForEachIntegerList(self):
        self.compareResourceEME("loops/forEachIntegerList.pec")

    def testForEachIntegerListWithIndex(self):
        self.compareResourceEME("loops/forEachIntegerListWithIndex.pec")

    def testForEachIntegerRange(self):
        self.compareResourceEME("loops/forEachIntegerRange.pec")

    def testForEachIntegerRangeWithIndex(self):
        self.compareResourceEME("loops/forEachIntegerRangeWithIndex.pec")

    def testForEachIntegerSet(self):
        self.compareResourceEME("loops/forEachIntegerSet.pec")

    def testForEachIntegerSetWithIndex(self):
        self.compareResourceEME("loops/forEachIntegerSetWithIndex.pec")

    def testForEachTimeRange(self):
        self.compareResourceEME("loops/forEachTimeRange.pec")

    def testForEachTimeRangeWithIndex(self):
        self.compareResourceEME("loops/forEachTimeRangeWithIndex.pec")

    def testForEachTupleList(self):
        self.compareResourceEME("loops/forEachTupleList.pec")

    def testForEachTupleListWithIndex(self):
        self.compareResourceEME("loops/forEachTupleListWithIndex.pec")

    def testForEachTupleSet(self):
        self.compareResourceEME("loops/forEachTupleSet.pec")

    def testForEachTupleSetWithIndex(self):
        self.compareResourceEME("loops/forEachTupleSetWithIndex.pec")

    def testWhile(self):
        self.compareResourceEME("loops/while.pec")

    def testWhileBreak(self):
        self.compareResourceEME("loops/whileBreak.pec")


