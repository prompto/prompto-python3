from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestLoops(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDoWhile(self):
        self.compareResourceEOE("loops/doWhile.e")

    def testForEachCharacterRange(self):
        self.compareResourceEOE("loops/forEachCharacterRange.e")

    def testForEachCharacterRangeWithIndex(self):
        self.compareResourceEOE("loops/forEachCharacterRangeWithIndex.e")

    def testForEachDateRange(self):
        self.compareResourceEOE("loops/forEachDateRange.e")

    def testForEachDateRangeWithIndex(self):
        self.compareResourceEOE("loops/forEachDateRangeWithIndex.e")

    def testForEachDictionaryItem(self):
        self.compareResourceEOE("loops/forEachDictionaryItem.e")

    def testForEachDictionaryItemWithIndex(self):
        self.compareResourceEOE("loops/forEachDictionaryItemWithIndex.e")

    def testForEachDictionaryKey(self):
        self.compareResourceEOE("loops/forEachDictionaryKey.e")

    def testForEachDictionaryKeyWithIndex(self):
        self.compareResourceEOE("loops/forEachDictionaryKeyWithIndex.e")

    def testForEachDictionaryValue(self):
        self.compareResourceEOE("loops/forEachDictionaryValue.e")

    def testForEachDictionaryValueWithIndex(self):
        self.compareResourceEOE("loops/forEachDictionaryValueWithIndex.e")

    def testForEachInstanceList(self):
        self.compareResourceEOE("loops/forEachInstanceList.e")

    def testForEachInstanceListWithIndex(self):
        self.compareResourceEOE("loops/forEachInstanceListWithIndex.e")

    def testForEachInstanceSet(self):
        self.compareResourceEOE("loops/forEachInstanceSet.e")

    def testForEachInstanceSetWithIndex(self):
        self.compareResourceEOE("loops/forEachInstanceSetWithIndex.e")

    def testForEachIntegerList(self):
        self.compareResourceEOE("loops/forEachIntegerList.e")

    def testForEachIntegerListWithIndex(self):
        self.compareResourceEOE("loops/forEachIntegerListWithIndex.e")

    def testForEachIntegerRange(self):
        self.compareResourceEOE("loops/forEachIntegerRange.e")

    def testForEachIntegerRangeWithIndex(self):
        self.compareResourceEOE("loops/forEachIntegerRangeWithIndex.e")

    def testForEachIntegerSet(self):
        self.compareResourceEOE("loops/forEachIntegerSet.e")

    def testForEachIntegerSetWithIndex(self):
        self.compareResourceEOE("loops/forEachIntegerSetWithIndex.e")

    def testForEachTimeRange(self):
        self.compareResourceEOE("loops/forEachTimeRange.e")

    def testForEachTimeRangeWithIndex(self):
        self.compareResourceEOE("loops/forEachTimeRangeWithIndex.e")

    def testForEachTupleList(self):
        self.compareResourceEOE("loops/forEachTupleList.e")

    def testForEachTupleListWithIndex(self):
        self.compareResourceEOE("loops/forEachTupleListWithIndex.e")

    def testForEachTupleSet(self):
        self.compareResourceEOE("loops/forEachTupleSet.e")

    def testForEachTupleSetWithIndex(self):
        self.compareResourceEOE("loops/forEachTupleSetWithIndex.e")

    def testWhile(self):
        self.compareResourceEOE("loops/while.e")


