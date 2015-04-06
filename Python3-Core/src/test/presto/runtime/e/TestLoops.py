from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestLoops(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDoWhile(self):
        self.checkOutput("loops/doWhile.pec")

    def testForEachCharacterRange(self):
        self.checkOutput("loops/forEachCharacterRange.pec")

    def testForEachCharacterRangeWithIndex(self):
        self.checkOutput("loops/forEachCharacterRangeWithIndex.pec")

    def testForEachDateRange(self):
        self.checkOutput("loops/forEachDateRange.pec")

    def testForEachDateRangeWithIndex(self):
        self.checkOutput("loops/forEachDateRangeWithIndex.pec")

    def testForEachDictionaryItem(self):
        self.checkOutput("loops/forEachDictionaryItem.pec")

    def testForEachDictionaryItemWithIndex(self):
        self.checkOutput("loops/forEachDictionaryItemWithIndex.pec")

    def testForEachDictionaryKey(self):
        self.checkOutput("loops/forEachDictionaryKey.pec")

    def testForEachDictionaryKeyWithIndex(self):
        self.checkOutput("loops/forEachDictionaryKeyWithIndex.pec")

    def testForEachDictionaryValue(self):
        self.checkOutput("loops/forEachDictionaryValue.pec")

    def testForEachDictionaryValueWithIndex(self):
        self.checkOutput("loops/forEachDictionaryValueWithIndex.pec")

    def testForEachInstanceList(self):
        self.checkOutput("loops/forEachInstanceList.pec")

    def testForEachInstanceListWithIndex(self):
        self.checkOutput("loops/forEachInstanceListWithIndex.pec")

    def testForEachInstanceSet(self):
        self.checkOutput("loops/forEachInstanceSet.pec")

    def testForEachInstanceSetWithIndex(self):
        self.checkOutput("loops/forEachInstanceSetWithIndex.pec")

    def testForEachIntegerList(self):
        self.checkOutput("loops/forEachIntegerList.pec")

    def testForEachIntegerListWithIndex(self):
        self.checkOutput("loops/forEachIntegerListWithIndex.pec")

    def testForEachIntegerRange(self):
        self.checkOutput("loops/forEachIntegerRange.pec")

    def testForEachIntegerRangeWithIndex(self):
        self.checkOutput("loops/forEachIntegerRangeWithIndex.pec")

    def testForEachIntegerSet(self):
        self.checkOutput("loops/forEachIntegerSet.pec")

    def testForEachIntegerSetWithIndex(self):
        self.checkOutput("loops/forEachIntegerSetWithIndex.pec")

    def testForEachTimeRange(self):
        self.checkOutput("loops/forEachTimeRange.pec")

    def testForEachTimeRangeWithIndex(self):
        self.checkOutput("loops/forEachTimeRangeWithIndex.pec")

    def testForEachTupleList(self):
        self.checkOutput("loops/forEachTupleList.pec")

    def testForEachTupleListWithIndex(self):
        self.checkOutput("loops/forEachTupleListWithIndex.pec")

    def testForEachTupleSet(self):
        self.checkOutput("loops/forEachTupleSet.pec")

    def testForEachTupleSetWithIndex(self):
        self.checkOutput("loops/forEachTupleSetWithIndex.pec")

    def testWhile(self):
        self.checkOutput("loops/while.pec")


