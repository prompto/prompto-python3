from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestStore(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAsyncFetchMany(self):
        self.compareResourceEOE("store/asyncFetchMany.pec")

    def testAsyncFetchOne(self):
        self.compareResourceEOE("store/asyncFetchOne.pec")

    def testAsyncStore(self):
        self.compareResourceEOE("store/asyncStore.pec")

    def testDeleteRecords(self):
        self.compareResourceEOE("store/deleteRecords.pec")

    def testFetchAnd(self):
        self.compareResourceEOE("store/fetchAnd.pec")

    def testFetchBoolean(self):
        self.compareResourceEOE("store/fetchBoolean.pec")

    def testFetchNotBoolean(self):
        self.compareResourceEOE("store/fetchNotBoolean.pec")

    def testFetchOr(self):
        self.compareResourceEOE("store/fetchOr.pec")

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


