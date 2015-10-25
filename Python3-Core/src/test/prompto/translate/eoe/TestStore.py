from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestStore(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testManyRecords(self):
        self.compareResourceEOE("store/manyRecords.pec")

    def testSimpleRecord(self):
        self.compareResourceEOE("store/simpleRecord.pec")

    def testSlicedRecords(self):
        self.compareResourceEOE("store/slicedRecords.pec")

    def testSortedRecords(self):
        self.compareResourceEOE("store/sortedRecords.pec")

    def testSubRecord(self):
        self.compareResourceEOE("store/subRecord.pec")


