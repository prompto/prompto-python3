from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestStore(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAsyncStore(self):
        self.compareResourceEOE("store/asyncStore.pec")

    def testDeleteRecords(self):
        self.compareResourceEOE("store/deleteRecords.pec")

    def testFlush(self):
        self.compareResourceEOE("store/flush.pec")

    def testListRecords(self):
        self.compareResourceEOE("store/listRecords.pec")

    def testManyRecords(self):
        self.compareResourceEOE("store/manyRecords.pec")

    def testManyUntypedRecords(self):
        self.compareResourceEOE("store/manyUntypedRecords.pec")

    def testSimpleRecord(self):
        self.compareResourceEOE("store/simpleRecord.pec")

    def testSlicedRecords(self):
        self.compareResourceEOE("store/slicedRecords.pec")

    def testSortedRecords(self):
        self.compareResourceEOE("store/sortedRecords.pec")

    def testSubRecord(self):
        self.compareResourceEOE("store/subRecord.pec")

    def testUntypedRecord(self):
        self.compareResourceEOE("store/untypedRecord.pec")


