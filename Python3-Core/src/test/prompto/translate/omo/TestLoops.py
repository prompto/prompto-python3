from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestLoops(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testDoWhile(self):
        self.compareResourceOMO("loops/doWhile.poc")

    def testDoWhileBreak(self):
        self.compareResourceOMO("loops/doWhileBreak.poc")

    def testEmbeddedForEach(self):
        self.compareResourceOMO("loops/embeddedForEach.poc")

    def testForEachBreak(self):
        self.compareResourceOMO("loops/forEachBreak.poc")

    def testForEachCharacterRange(self):
        self.compareResourceOMO("loops/forEachCharacterRange.poc")

    def testForEachCharacterRangeWithIndex(self):
        self.compareResourceOMO("loops/forEachCharacterRangeWithIndex.poc")

    def testForEachDateRange(self):
        self.compareResourceOMO("loops/forEachDateRange.poc")

    def testForEachDateRangeWithIndex(self):
        self.compareResourceOMO("loops/forEachDateRangeWithIndex.poc")

    def testForEachDictionaryItem(self):
        self.compareResourceOMO("loops/forEachDictionaryItem.poc")

    def testForEachDictionaryItemWithIndex(self):
        self.compareResourceOMO("loops/forEachDictionaryItemWithIndex.poc")

    def testForEachDictionaryKey(self):
        self.compareResourceOMO("loops/forEachDictionaryKey.poc")

    def testForEachDictionaryKeyWithIndex(self):
        self.compareResourceOMO("loops/forEachDictionaryKeyWithIndex.poc")

    def testForEachDictionaryValue(self):
        self.compareResourceOMO("loops/forEachDictionaryValue.poc")

    def testForEachDictionaryValueWithIndex(self):
        self.compareResourceOMO("loops/forEachDictionaryValueWithIndex.poc")

    def testForEachInstanceList(self):
        self.compareResourceOMO("loops/forEachInstanceList.poc")

    def testForEachInstanceListWithIndex(self):
        self.compareResourceOMO("loops/forEachInstanceListWithIndex.poc")

    def testForEachInstanceSet(self):
        self.compareResourceOMO("loops/forEachInstanceSet.poc")

    def testForEachInstanceSetWithIndex(self):
        self.compareResourceOMO("loops/forEachInstanceSetWithIndex.poc")

    def testForEachIntegerList(self):
        self.compareResourceOMO("loops/forEachIntegerList.poc")

    def testForEachIntegerListWithIndex(self):
        self.compareResourceOMO("loops/forEachIntegerListWithIndex.poc")

    def testForEachIntegerRange(self):
        self.compareResourceOMO("loops/forEachIntegerRange.poc")

    def testForEachIntegerRangeWithIndex(self):
        self.compareResourceOMO("loops/forEachIntegerRangeWithIndex.poc")

    def testForEachIntegerSet(self):
        self.compareResourceOMO("loops/forEachIntegerSet.poc")

    def testForEachIntegerSetWithIndex(self):
        self.compareResourceOMO("loops/forEachIntegerSetWithIndex.poc")

    def testForEachTextCharacter(self):
        self.compareResourceOMO("loops/forEachTextCharacter.poc")

    def testForEachTimeRange(self):
        self.compareResourceOMO("loops/forEachTimeRange.poc")

    def testForEachTimeRangeWithIndex(self):
        self.compareResourceOMO("loops/forEachTimeRangeWithIndex.poc")

    def testForEachTupleList(self):
        self.compareResourceOMO("loops/forEachTupleList.poc")

    def testForEachTupleListWithIndex(self):
        self.compareResourceOMO("loops/forEachTupleListWithIndex.poc")

    def testForEachTupleSet(self):
        self.compareResourceOMO("loops/forEachTupleSet.poc")

    def testForEachTupleSetWithIndex(self):
        self.compareResourceOMO("loops/forEachTupleSetWithIndex.poc")

    def testWhile(self):
        self.compareResourceOMO("loops/while.poc")

    def testWhileBreak(self):
        self.compareResourceOMO("loops/whileBreak.poc")


