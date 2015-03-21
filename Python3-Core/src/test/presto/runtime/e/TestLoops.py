from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestLoops(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDoWhile(self):
        self.checkOutput("loops/doWhile.e")

    def testForEachCharacterRange(self):
        self.checkOutput("loops/forEachCharacterRange.e")

    def testForEachCharacterRangeWithIndex(self):
        self.checkOutput("loops/forEachCharacterRangeWithIndex.e")

    def testForEachDateRange(self):
        self.checkOutput("loops/forEachDateRange.e")

    def testForEachDateRangeWithIndex(self):
        self.checkOutput("loops/forEachDateRangeWithIndex.e")

    def testForEachDictionaryItem(self):
        self.checkOutput("loops/forEachDictionaryItem.e")

    def testForEachDictionaryItemWithIndex(self):
        self.checkOutput("loops/forEachDictionaryItemWithIndex.e")

    def testForEachDictionaryKey(self):
        self.checkOutput("loops/forEachDictionaryKey.e")

    def testForEachDictionaryKeyWithIndex(self):
        self.checkOutput("loops/forEachDictionaryKeyWithIndex.e")

    def testForEachDictionaryValue(self):
        self.checkOutput("loops/forEachDictionaryValue.e")

    def testForEachDictionaryValueWithIndex(self):
        self.checkOutput("loops/forEachDictionaryValueWithIndex.e")

    def testForEachInstanceList(self):
        self.checkOutput("loops/forEachInstanceList.e")

    def testForEachInstanceListWithIndex(self):
        self.checkOutput("loops/forEachInstanceListWithIndex.e")

    def testForEachInstanceSet(self):
        self.checkOutput("loops/forEachInstanceSet.e")

    def testForEachInstanceSetWithIndex(self):
        self.checkOutput("loops/forEachInstanceSetWithIndex.e")

    def testForEachIntegerList(self):
        self.checkOutput("loops/forEachIntegerList.e")

    def testForEachIntegerListWithIndex(self):
        self.checkOutput("loops/forEachIntegerListWithIndex.e")

    def testForEachIntegerRange(self):
        self.checkOutput("loops/forEachIntegerRange.e")

    def testForEachIntegerRangeWithIndex(self):
        self.checkOutput("loops/forEachIntegerRangeWithIndex.e")

    def testForEachIntegerSet(self):
        self.checkOutput("loops/forEachIntegerSet.e")

    def testForEachIntegerSetWithIndex(self):
        self.checkOutput("loops/forEachIntegerSetWithIndex.e")

    def testForEachTimeRange(self):
        self.checkOutput("loops/forEachTimeRange.e")

    def testForEachTimeRangeWithIndex(self):
        self.checkOutput("loops/forEachTimeRangeWithIndex.e")

    def testForEachTupleList(self):
        self.checkOutput("loops/forEachTupleList.e")

    def testForEachTupleListWithIndex(self):
        self.checkOutput("loops/forEachTupleListWithIndex.e")

    def testForEachTupleSet(self):
        self.checkOutput("loops/forEachTupleSet.e")

    def testForEachTupleSetWithIndex(self):
        self.checkOutput("loops/forEachTupleSetWithIndex.e")

    def testWhile(self):
        self.checkOutput("loops/while.e")


