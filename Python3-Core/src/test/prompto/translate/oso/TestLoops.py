from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestLoops(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDoWhile(self):
        self.compareResourceOSO("loops/doWhile.poc")

    def testEmbeddedForEach(self):
        self.compareResourceOSO("loops/embeddedForEach.poc")

    def testForEachCharacterRange(self):
        self.compareResourceOSO("loops/forEachCharacterRange.poc")

    def testForEachCharacterRangeWithIndex(self):
        self.compareResourceOSO("loops/forEachCharacterRangeWithIndex.poc")

    def testForEachDateRange(self):
        self.compareResourceOSO("loops/forEachDateRange.poc")

    def testForEachDateRangeWithIndex(self):
        self.compareResourceOSO("loops/forEachDateRangeWithIndex.poc")

    def testForEachDictionaryItem(self):
        self.compareResourceOSO("loops/forEachDictionaryItem.poc")

    def testForEachDictionaryItemWithIndex(self):
        self.compareResourceOSO("loops/forEachDictionaryItemWithIndex.poc")

    def testForEachDictionaryKey(self):
        self.compareResourceOSO("loops/forEachDictionaryKey.poc")

    def testForEachDictionaryKeyWithIndex(self):
        self.compareResourceOSO("loops/forEachDictionaryKeyWithIndex.poc")

    def testForEachDictionaryValue(self):
        self.compareResourceOSO("loops/forEachDictionaryValue.poc")

    def testForEachDictionaryValueWithIndex(self):
        self.compareResourceOSO("loops/forEachDictionaryValueWithIndex.poc")

    def testForEachInstanceList(self):
        self.compareResourceOSO("loops/forEachInstanceList.poc")

    def testForEachInstanceListWithIndex(self):
        self.compareResourceOSO("loops/forEachInstanceListWithIndex.poc")

    def testForEachInstanceSet(self):
        self.compareResourceOSO("loops/forEachInstanceSet.poc")

    def testForEachInstanceSetWithIndex(self):
        self.compareResourceOSO("loops/forEachInstanceSetWithIndex.poc")

    def testForEachIntegerList(self):
        self.compareResourceOSO("loops/forEachIntegerList.poc")

    def testForEachIntegerListWithIndex(self):
        self.compareResourceOSO("loops/forEachIntegerListWithIndex.poc")

    def testForEachIntegerRange(self):
        self.compareResourceOSO("loops/forEachIntegerRange.poc")

    def testForEachIntegerRangeWithIndex(self):
        self.compareResourceOSO("loops/forEachIntegerRangeWithIndex.poc")

    def testForEachIntegerSet(self):
        self.compareResourceOSO("loops/forEachIntegerSet.poc")

    def testForEachIntegerSetWithIndex(self):
        self.compareResourceOSO("loops/forEachIntegerSetWithIndex.poc")

    def testForEachTimeRange(self):
        self.compareResourceOSO("loops/forEachTimeRange.poc")

    def testForEachTimeRangeWithIndex(self):
        self.compareResourceOSO("loops/forEachTimeRangeWithIndex.poc")

    def testForEachTupleList(self):
        self.compareResourceOSO("loops/forEachTupleList.poc")

    def testForEachTupleListWithIndex(self):
        self.compareResourceOSO("loops/forEachTupleListWithIndex.poc")

    def testForEachTupleSet(self):
        self.compareResourceOSO("loops/forEachTupleSet.poc")

    def testForEachTupleSetWithIndex(self):
        self.compareResourceOSO("loops/forEachTupleSetWithIndex.poc")

    def testWhile(self):
        self.compareResourceOSO("loops/while.poc")


