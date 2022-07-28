from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestLoops(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDoWhile(self):
        self.compareResourceOEO("loops/doWhile.poc")

    def testDoWhileBreak(self):
        self.compareResourceOEO("loops/doWhileBreak.poc")

    def testEmbeddedForEach(self):
        self.compareResourceOEO("loops/embeddedForEach.poc")

    def testForEachBreak(self):
        self.compareResourceOEO("loops/forEachBreak.poc")

    def testForEachCharacterRange(self):
        self.compareResourceOEO("loops/forEachCharacterRange.poc")

    def testForEachCharacterRangeWithIndex(self):
        self.compareResourceOEO("loops/forEachCharacterRangeWithIndex.poc")

    def testForEachDateRange(self):
        self.compareResourceOEO("loops/forEachDateRange.poc")

    def testForEachDateRangeWithIndex(self):
        self.compareResourceOEO("loops/forEachDateRangeWithIndex.poc")

    def testForEachDictionaryItem(self):
        self.compareResourceOEO("loops/forEachDictionaryItem.poc")

    def testForEachDictionaryItemWithIndex(self):
        self.compareResourceOEO("loops/forEachDictionaryItemWithIndex.poc")

    def testForEachDictionaryKey(self):
        self.compareResourceOEO("loops/forEachDictionaryKey.poc")

    def testForEachDictionaryKeyWithIndex(self):
        self.compareResourceOEO("loops/forEachDictionaryKeyWithIndex.poc")

    def testForEachDictionaryValue(self):
        self.compareResourceOEO("loops/forEachDictionaryValue.poc")

    def testForEachDictionaryValueWithIndex(self):
        self.compareResourceOEO("loops/forEachDictionaryValueWithIndex.poc")

    def testForEachInstanceList(self):
        self.compareResourceOEO("loops/forEachInstanceList.poc")

    def testForEachInstanceListWithIndex(self):
        self.compareResourceOEO("loops/forEachInstanceListWithIndex.poc")

    def testForEachInstanceSet(self):
        self.compareResourceOEO("loops/forEachInstanceSet.poc")

    def testForEachInstanceSetWithIndex(self):
        self.compareResourceOEO("loops/forEachInstanceSetWithIndex.poc")

    def testForEachIntegerList(self):
        self.compareResourceOEO("loops/forEachIntegerList.poc")

    def testForEachIntegerListWithIndex(self):
        self.compareResourceOEO("loops/forEachIntegerListWithIndex.poc")

    def testForEachIntegerRange(self):
        self.compareResourceOEO("loops/forEachIntegerRange.poc")

    def testForEachIntegerRangeWithIndex(self):
        self.compareResourceOEO("loops/forEachIntegerRangeWithIndex.poc")

    def testForEachIntegerSet(self):
        self.compareResourceOEO("loops/forEachIntegerSet.poc")

    def testForEachIntegerSetWithIndex(self):
        self.compareResourceOEO("loops/forEachIntegerSetWithIndex.poc")

    def testForEachTextCharacter(self):
        self.compareResourceOEO("loops/forEachTextCharacter.poc")

    def testForEachTimeRange(self):
        self.compareResourceOEO("loops/forEachTimeRange.poc")

    def testForEachTimeRangeWithIndex(self):
        self.compareResourceOEO("loops/forEachTimeRangeWithIndex.poc")

    def testForEachTupleList(self):
        self.compareResourceOEO("loops/forEachTupleList.poc")

    def testForEachTupleListWithIndex(self):
        self.compareResourceOEO("loops/forEachTupleListWithIndex.poc")

    def testForEachTupleSet(self):
        self.compareResourceOEO("loops/forEachTupleSet.poc")

    def testForEachTupleSetWithIndex(self):
        self.compareResourceOEO("loops/forEachTupleSetWithIndex.poc")

    def testWhile(self):
        self.compareResourceOEO("loops/while.poc")

    def testWhileBreak(self):
        self.compareResourceOEO("loops/whileBreak.poc")


