from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestLoops(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDoWhile(self):
        self.compareResourceEOE("loops/doWhile.pec")

    def testForEachCharacterRange(self):
        self.compareResourceEOE("loops/forEachCharacterRange.pec")

    def testForEachCharacterRangeWithIndex(self):
        self.compareResourceEOE("loops/forEachCharacterRangeWithIndex.pec")

    def testForEachDateRange(self):
        self.compareResourceEOE("loops/forEachDateRange.pec")

    def testForEachDateRangeWithIndex(self):
        self.compareResourceEOE("loops/forEachDateRangeWithIndex.pec")

    def testForEachDictionaryItem(self):
        self.compareResourceEOE("loops/forEachDictionaryItem.pec")

    def testForEachDictionaryItemWithIndex(self):
        self.compareResourceEOE("loops/forEachDictionaryItemWithIndex.pec")

    def testForEachDictionaryKey(self):
        self.compareResourceEOE("loops/forEachDictionaryKey.pec")

    def testForEachDictionaryKeyWithIndex(self):
        self.compareResourceEOE("loops/forEachDictionaryKeyWithIndex.pec")

    def testForEachDictionaryValue(self):
        self.compareResourceEOE("loops/forEachDictionaryValue.pec")

    def testForEachDictionaryValueWithIndex(self):
        self.compareResourceEOE("loops/forEachDictionaryValueWithIndex.pec")

    def testForEachInstanceList(self):
        self.compareResourceEOE("loops/forEachInstanceList.pec")

    def testForEachInstanceListWithIndex(self):
        self.compareResourceEOE("loops/forEachInstanceListWithIndex.pec")

    def testForEachInstanceSet(self):
        self.compareResourceEOE("loops/forEachInstanceSet.pec")

    def testForEachInstanceSetWithIndex(self):
        self.compareResourceEOE("loops/forEachInstanceSetWithIndex.pec")

    def testForEachIntegerList(self):
        self.compareResourceEOE("loops/forEachIntegerList.pec")

    def testForEachIntegerListWithIndex(self):
        self.compareResourceEOE("loops/forEachIntegerListWithIndex.pec")

    def testForEachIntegerRange(self):
        self.compareResourceEOE("loops/forEachIntegerRange.pec")

    def testForEachIntegerRangeWithIndex(self):
        self.compareResourceEOE("loops/forEachIntegerRangeWithIndex.pec")

    def testForEachIntegerSet(self):
        self.compareResourceEOE("loops/forEachIntegerSet.pec")

    def testForEachIntegerSetWithIndex(self):
        self.compareResourceEOE("loops/forEachIntegerSetWithIndex.pec")

    def testForEachTimeRange(self):
        self.compareResourceEOE("loops/forEachTimeRange.pec")

    def testForEachTimeRangeWithIndex(self):
        self.compareResourceEOE("loops/forEachTimeRangeWithIndex.pec")

    def testForEachTupleList(self):
        self.compareResourceEOE("loops/forEachTupleList.pec")

    def testForEachTupleListWithIndex(self):
        self.compareResourceEOE("loops/forEachTupleListWithIndex.pec")

    def testForEachTupleSet(self):
        self.compareResourceEOE("loops/forEachTupleSet.pec")

    def testForEachTupleSetWithIndex(self):
        self.compareResourceEOE("loops/forEachTupleSetWithIndex.pec")

    def testWhile(self):
        self.compareResourceEOE("loops/while.pec")


