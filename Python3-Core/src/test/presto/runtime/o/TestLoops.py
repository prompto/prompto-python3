from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestLoops(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDoWhile(self):
        self.checkOutput("loops/doWhile.o")

    def testForEachCharacterRange(self):
        self.checkOutput("loops/forEachCharacterRange.o")

    def testForEachCharacterRangeWithIndex(self):
        self.checkOutput("loops/forEachCharacterRangeWithIndex.o")

    def testForEachDateRange(self):
        self.checkOutput("loops/forEachDateRange.o")

    def testForEachDateRangeWithIndex(self):
        self.checkOutput("loops/forEachDateRangeWithIndex.o")

    def testForEachDictionaryItem(self):
        self.checkOutput("loops/forEachDictionaryItem.o")

    def testForEachDictionaryItemWithIndex(self):
        self.checkOutput("loops/forEachDictionaryItemWithIndex.o")

    def testForEachDictionaryKey(self):
        self.checkOutput("loops/forEachDictionaryKey.o")

    def testForEachDictionaryKeyWithIndex(self):
        self.checkOutput("loops/forEachDictionaryKeyWithIndex.o")

    def testForEachDictionaryValue(self):
        self.checkOutput("loops/forEachDictionaryValue.o")

    def testForEachDictionaryValueWithIndex(self):
        self.checkOutput("loops/forEachDictionaryValueWithIndex.o")

    def testForEachInstanceList(self):
        self.checkOutput("loops/forEachInstanceList.o")

    def testForEachInstanceListWithIndex(self):
        self.checkOutput("loops/forEachInstanceListWithIndex.o")

    def testForEachInstanceSet(self):
        self.checkOutput("loops/forEachInstanceSet.o")

    def testForEachInstanceSetWithIndex(self):
        self.checkOutput("loops/forEachInstanceSetWithIndex.o")

    def testForEachIntegerList(self):
        self.checkOutput("loops/forEachIntegerList.o")

    def testForEachIntegerListWithIndex(self):
        self.checkOutput("loops/forEachIntegerListWithIndex.o")

    def testForEachIntegerRange(self):
        self.checkOutput("loops/forEachIntegerRange.o")

    def testForEachIntegerRangeWithIndex(self):
        self.checkOutput("loops/forEachIntegerRangeWithIndex.o")

    def testForEachIntegerSet(self):
        self.checkOutput("loops/forEachIntegerSet.o")

    def testForEachIntegerSetWithIndex(self):
        self.checkOutput("loops/forEachIntegerSetWithIndex.o")

    def testForEachTimeRange(self):
        self.checkOutput("loops/forEachTimeRange.o")

    def testForEachTimeRangeWithIndex(self):
        self.checkOutput("loops/forEachTimeRangeWithIndex.o")

    def testForEachTupleList(self):
        self.checkOutput("loops/forEachTupleList.o")

    def testForEachTupleListWithIndex(self):
        self.checkOutput("loops/forEachTupleListWithIndex.o")

    def testForEachTupleSet(self):
        self.checkOutput("loops/forEachTupleSet.o")

    def testForEachTupleSetWithIndex(self):
        self.checkOutput("loops/forEachTupleSetWithIndex.o")

    def testWhile(self):
        self.checkOutput("loops/while.o")


