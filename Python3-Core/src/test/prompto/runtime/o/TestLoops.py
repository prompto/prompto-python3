from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestLoops(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDoWhile(self):
        self.checkOutput("loops/doWhile.poc")

    def testForEachCharacterRange(self):
        self.checkOutput("loops/forEachCharacterRange.poc")

    def testForEachCharacterRangeWithIndex(self):
        self.checkOutput("loops/forEachCharacterRangeWithIndex.poc")

    def testForEachDateRange(self):
        self.checkOutput("loops/forEachDateRange.poc")

    def testForEachDateRangeWithIndex(self):
        self.checkOutput("loops/forEachDateRangeWithIndex.poc")

    def testForEachDictionaryItem(self):
        self.checkOutput("loops/forEachDictionaryItem.poc")

    def testForEachDictionaryItemWithIndex(self):
        self.checkOutput("loops/forEachDictionaryItemWithIndex.poc")

    def testForEachDictionaryKey(self):
        self.checkOutput("loops/forEachDictionaryKey.poc")

    def testForEachDictionaryKeyWithIndex(self):
        self.checkOutput("loops/forEachDictionaryKeyWithIndex.poc")

    def testForEachDictionaryValue(self):
        self.checkOutput("loops/forEachDictionaryValue.poc")

    def testForEachDictionaryValueWithIndex(self):
        self.checkOutput("loops/forEachDictionaryValueWithIndex.poc")

    def testForEachInstanceList(self):
        self.checkOutput("loops/forEachInstanceList.poc")

    def testForEachInstanceListWithIndex(self):
        self.checkOutput("loops/forEachInstanceListWithIndex.poc")

    def testForEachInstanceSet(self):
        self.checkOutput("loops/forEachInstanceSet.poc")

    def testForEachInstanceSetWithIndex(self):
        self.checkOutput("loops/forEachInstanceSetWithIndex.poc")

    def testForEachIntegerList(self):
        self.checkOutput("loops/forEachIntegerList.poc")

    def testForEachIntegerListWithIndex(self):
        self.checkOutput("loops/forEachIntegerListWithIndex.poc")

    def testForEachIntegerRange(self):
        self.checkOutput("loops/forEachIntegerRange.poc")

    def testForEachIntegerRangeWithIndex(self):
        self.checkOutput("loops/forEachIntegerRangeWithIndex.poc")

    def testForEachIntegerSet(self):
        self.checkOutput("loops/forEachIntegerSet.poc")

    def testForEachIntegerSetWithIndex(self):
        self.checkOutput("loops/forEachIntegerSetWithIndex.poc")

    def testForEachTimeRange(self):
        self.checkOutput("loops/forEachTimeRange.poc")

    def testForEachTimeRangeWithIndex(self):
        self.checkOutput("loops/forEachTimeRangeWithIndex.poc")

    def testForEachTupleList(self):
        self.checkOutput("loops/forEachTupleList.poc")

    def testForEachTupleListWithIndex(self):
        self.checkOutput("loops/forEachTupleListWithIndex.poc")

    def testForEachTupleSet(self):
        self.checkOutput("loops/forEachTupleSet.poc")

    def testForEachTupleSetWithIndex(self):
        self.checkOutput("loops/forEachTupleSetWithIndex.poc")

    def testWhile(self):
        self.checkOutput("loops/while.poc")


