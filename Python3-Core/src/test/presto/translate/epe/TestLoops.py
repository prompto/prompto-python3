from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestLoops(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDoWhile(self):
        self.compareResourceEPE("loops/doWhile.e")

    def testForEachCharacterRange(self):
        self.compareResourceEPE("loops/forEachCharacterRange.e")

    def testForEachCharacterRangeWithIndex(self):
        self.compareResourceEPE("loops/forEachCharacterRangeWithIndex.e")

    def testForEachDateRange(self):
        self.compareResourceEPE("loops/forEachDateRange.e")

    def testForEachDateRangeWithIndex(self):
        self.compareResourceEPE("loops/forEachDateRangeWithIndex.e")

    def testForEachDictionaryItem(self):
        self.compareResourceEPE("loops/forEachDictionaryItem.e")

    def testForEachDictionaryItemWithIndex(self):
        self.compareResourceEPE("loops/forEachDictionaryItemWithIndex.e")

    def testForEachDictionaryKey(self):
        self.compareResourceEPE("loops/forEachDictionaryKey.e")

    def testForEachDictionaryKeyWithIndex(self):
        self.compareResourceEPE("loops/forEachDictionaryKeyWithIndex.e")

    def testForEachDictionaryValue(self):
        self.compareResourceEPE("loops/forEachDictionaryValue.e")

    def testForEachDictionaryValueWithIndex(self):
        self.compareResourceEPE("loops/forEachDictionaryValueWithIndex.e")

    def testForEachInstanceList(self):
        self.compareResourceEPE("loops/forEachInstanceList.e")

    def testForEachInstanceListWithIndex(self):
        self.compareResourceEPE("loops/forEachInstanceListWithIndex.e")

    def testForEachInstanceSet(self):
        self.compareResourceEPE("loops/forEachInstanceSet.e")

    def testForEachInstanceSetWithIndex(self):
        self.compareResourceEPE("loops/forEachInstanceSetWithIndex.e")

    def testForEachIntegerList(self):
        self.compareResourceEPE("loops/forEachIntegerList.e")

    def testForEachIntegerListWithIndex(self):
        self.compareResourceEPE("loops/forEachIntegerListWithIndex.e")

    def testForEachIntegerRange(self):
        self.compareResourceEPE("loops/forEachIntegerRange.e")

    def testForEachIntegerRangeWithIndex(self):
        self.compareResourceEPE("loops/forEachIntegerRangeWithIndex.e")

    def testForEachIntegerSet(self):
        self.compareResourceEPE("loops/forEachIntegerSet.e")

    def testForEachIntegerSetWithIndex(self):
        self.compareResourceEPE("loops/forEachIntegerSetWithIndex.e")

    def testForEachTimeRange(self):
        self.compareResourceEPE("loops/forEachTimeRange.e")

    def testForEachTimeRangeWithIndex(self):
        self.compareResourceEPE("loops/forEachTimeRangeWithIndex.e")

    def testForEachTupleList(self):
        self.compareResourceEPE("loops/forEachTupleList.e")

    def testForEachTupleListWithIndex(self):
        self.compareResourceEPE("loops/forEachTupleListWithIndex.e")

    def testForEachTupleSet(self):
        self.compareResourceEPE("loops/forEachTupleSet.e")

    def testForEachTupleSetWithIndex(self):
        self.compareResourceEPE("loops/forEachTupleSetWithIndex.e")

    def testWhile(self):
        self.compareResourceEPE("loops/while.e")


