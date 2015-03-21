from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestLoops(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDoWhile(self):
        self.compareResourceOEO("loops/doWhile.o")

    def testForEachCharacterRange(self):
        self.compareResourceOEO("loops/forEachCharacterRange.o")

    def testForEachCharacterRangeWithIndex(self):
        self.compareResourceOEO("loops/forEachCharacterRangeWithIndex.o")

    def testForEachDateRange(self):
        self.compareResourceOEO("loops/forEachDateRange.o")

    def testForEachDateRangeWithIndex(self):
        self.compareResourceOEO("loops/forEachDateRangeWithIndex.o")

    def testForEachDictionaryItem(self):
        self.compareResourceOEO("loops/forEachDictionaryItem.o")

    def testForEachDictionaryItemWithIndex(self):
        self.compareResourceOEO("loops/forEachDictionaryItemWithIndex.o")

    def testForEachDictionaryKey(self):
        self.compareResourceOEO("loops/forEachDictionaryKey.o")

    def testForEachDictionaryKeyWithIndex(self):
        self.compareResourceOEO("loops/forEachDictionaryKeyWithIndex.o")

    def testForEachDictionaryValue(self):
        self.compareResourceOEO("loops/forEachDictionaryValue.o")

    def testForEachDictionaryValueWithIndex(self):
        self.compareResourceOEO("loops/forEachDictionaryValueWithIndex.o")

    def testForEachInstanceList(self):
        self.compareResourceOEO("loops/forEachInstanceList.o")

    def testForEachInstanceListWithIndex(self):
        self.compareResourceOEO("loops/forEachInstanceListWithIndex.o")

    def testForEachInstanceSet(self):
        self.compareResourceOEO("loops/forEachInstanceSet.o")

    def testForEachInstanceSetWithIndex(self):
        self.compareResourceOEO("loops/forEachInstanceSetWithIndex.o")

    def testForEachIntegerList(self):
        self.compareResourceOEO("loops/forEachIntegerList.o")

    def testForEachIntegerListWithIndex(self):
        self.compareResourceOEO("loops/forEachIntegerListWithIndex.o")

    def testForEachIntegerRange(self):
        self.compareResourceOEO("loops/forEachIntegerRange.o")

    def testForEachIntegerRangeWithIndex(self):
        self.compareResourceOEO("loops/forEachIntegerRangeWithIndex.o")

    def testForEachIntegerSet(self):
        self.compareResourceOEO("loops/forEachIntegerSet.o")

    def testForEachIntegerSetWithIndex(self):
        self.compareResourceOEO("loops/forEachIntegerSetWithIndex.o")

    def testForEachTimeRange(self):
        self.compareResourceOEO("loops/forEachTimeRange.o")

    def testForEachTimeRangeWithIndex(self):
        self.compareResourceOEO("loops/forEachTimeRangeWithIndex.o")

    def testForEachTupleList(self):
        self.compareResourceOEO("loops/forEachTupleList.o")

    def testForEachTupleListWithIndex(self):
        self.compareResourceOEO("loops/forEachTupleListWithIndex.o")

    def testForEachTupleSet(self):
        self.compareResourceOEO("loops/forEachTupleSet.o")

    def testForEachTupleSetWithIndex(self):
        self.compareResourceOEO("loops/forEachTupleSetWithIndex.o")

    def testWhile(self):
        self.compareResourceOEO("loops/while.o")


