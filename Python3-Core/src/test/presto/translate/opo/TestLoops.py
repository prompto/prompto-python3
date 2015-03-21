from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestLoops(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDoWhile(self):
        self.compareResourceOPO("loops/doWhile.o")

    def testForEachCharacterRange(self):
        self.compareResourceOPO("loops/forEachCharacterRange.o")

    def testForEachCharacterRangeWithIndex(self):
        self.compareResourceOPO("loops/forEachCharacterRangeWithIndex.o")

    def testForEachDateRange(self):
        self.compareResourceOPO("loops/forEachDateRange.o")

    def testForEachDateRangeWithIndex(self):
        self.compareResourceOPO("loops/forEachDateRangeWithIndex.o")

    def testForEachDictionaryItem(self):
        self.compareResourceOPO("loops/forEachDictionaryItem.o")

    def testForEachDictionaryItemWithIndex(self):
        self.compareResourceOPO("loops/forEachDictionaryItemWithIndex.o")

    def testForEachDictionaryKey(self):
        self.compareResourceOPO("loops/forEachDictionaryKey.o")

    def testForEachDictionaryKeyWithIndex(self):
        self.compareResourceOPO("loops/forEachDictionaryKeyWithIndex.o")

    def testForEachDictionaryValue(self):
        self.compareResourceOPO("loops/forEachDictionaryValue.o")

    def testForEachDictionaryValueWithIndex(self):
        self.compareResourceOPO("loops/forEachDictionaryValueWithIndex.o")

    def testForEachInstanceList(self):
        self.compareResourceOPO("loops/forEachInstanceList.o")

    def testForEachInstanceListWithIndex(self):
        self.compareResourceOPO("loops/forEachInstanceListWithIndex.o")

    def testForEachInstanceSet(self):
        self.compareResourceOPO("loops/forEachInstanceSet.o")

    def testForEachInstanceSetWithIndex(self):
        self.compareResourceOPO("loops/forEachInstanceSetWithIndex.o")

    def testForEachIntegerList(self):
        self.compareResourceOPO("loops/forEachIntegerList.o")

    def testForEachIntegerListWithIndex(self):
        self.compareResourceOPO("loops/forEachIntegerListWithIndex.o")

    def testForEachIntegerRange(self):
        self.compareResourceOPO("loops/forEachIntegerRange.o")

    def testForEachIntegerRangeWithIndex(self):
        self.compareResourceOPO("loops/forEachIntegerRangeWithIndex.o")

    def testForEachIntegerSet(self):
        self.compareResourceOPO("loops/forEachIntegerSet.o")

    def testForEachIntegerSetWithIndex(self):
        self.compareResourceOPO("loops/forEachIntegerSetWithIndex.o")

    def testForEachTimeRange(self):
        self.compareResourceOPO("loops/forEachTimeRange.o")

    def testForEachTimeRangeWithIndex(self):
        self.compareResourceOPO("loops/forEachTimeRangeWithIndex.o")

    def testForEachTupleList(self):
        self.compareResourceOPO("loops/forEachTupleList.o")

    def testForEachTupleListWithIndex(self):
        self.compareResourceOPO("loops/forEachTupleListWithIndex.o")

    def testForEachTupleSet(self):
        self.compareResourceOPO("loops/forEachTupleSet.o")

    def testForEachTupleSetWithIndex(self):
        self.compareResourceOPO("loops/forEachTupleSetWithIndex.o")

    def testWhile(self):
        self.compareResourceOPO("loops/while.o")


