from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestLoops(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDoWhile(self):
        self.compareResourceESE("loops/doWhile.pec")

    def testForEachCharacterRange(self):
        self.compareResourceESE("loops/forEachCharacterRange.pec")

    def testForEachCharacterRangeWithIndex(self):
        self.compareResourceESE("loops/forEachCharacterRangeWithIndex.pec")

    def testForEachDateRange(self):
        self.compareResourceESE("loops/forEachDateRange.pec")

    def testForEachDateRangeWithIndex(self):
        self.compareResourceESE("loops/forEachDateRangeWithIndex.pec")

    def testForEachDictionaryItem(self):
        self.compareResourceESE("loops/forEachDictionaryItem.pec")

    def testForEachDictionaryItemWithIndex(self):
        self.compareResourceESE("loops/forEachDictionaryItemWithIndex.pec")

    def testForEachDictionaryKey(self):
        self.compareResourceESE("loops/forEachDictionaryKey.pec")

    def testForEachDictionaryKeyWithIndex(self):
        self.compareResourceESE("loops/forEachDictionaryKeyWithIndex.pec")

    def testForEachDictionaryValue(self):
        self.compareResourceESE("loops/forEachDictionaryValue.pec")

    def testForEachDictionaryValueWithIndex(self):
        self.compareResourceESE("loops/forEachDictionaryValueWithIndex.pec")

    def testForEachInstanceList(self):
        self.compareResourceESE("loops/forEachInstanceList.pec")

    def testForEachInstanceListWithIndex(self):
        self.compareResourceESE("loops/forEachInstanceListWithIndex.pec")

    def testForEachInstanceSet(self):
        self.compareResourceESE("loops/forEachInstanceSet.pec")

    def testForEachInstanceSetWithIndex(self):
        self.compareResourceESE("loops/forEachInstanceSetWithIndex.pec")

    def testForEachIntegerList(self):
        self.compareResourceESE("loops/forEachIntegerList.pec")

    def testForEachIntegerListWithIndex(self):
        self.compareResourceESE("loops/forEachIntegerListWithIndex.pec")

    def testForEachIntegerRange(self):
        self.compareResourceESE("loops/forEachIntegerRange.pec")

    def testForEachIntegerRangeWithIndex(self):
        self.compareResourceESE("loops/forEachIntegerRangeWithIndex.pec")

    def testForEachIntegerSet(self):
        self.compareResourceESE("loops/forEachIntegerSet.pec")

    def testForEachIntegerSetWithIndex(self):
        self.compareResourceESE("loops/forEachIntegerSetWithIndex.pec")

    def testForEachTimeRange(self):
        self.compareResourceESE("loops/forEachTimeRange.pec")

    def testForEachTimeRangeWithIndex(self):
        self.compareResourceESE("loops/forEachTimeRangeWithIndex.pec")

    def testForEachTupleList(self):
        self.compareResourceESE("loops/forEachTupleList.pec")

    def testForEachTupleListWithIndex(self):
        self.compareResourceESE("loops/forEachTupleListWithIndex.pec")

    def testForEachTupleSet(self):
        self.compareResourceESE("loops/forEachTupleSet.pec")

    def testForEachTupleSetWithIndex(self):
        self.compareResourceESE("loops/forEachTupleSetWithIndex.pec")

    def testWhile(self):
        self.compareResourceESE("loops/while.pec")


