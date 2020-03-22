from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestStore(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAsyncFetchMany(self):
        self.compareResourceEME("store/asyncFetchMany.pec")

    def testAsyncFetchOne(self):
        self.compareResourceEME("store/asyncFetchOne.pec")

    def testAsyncStore(self):
        self.compareResourceEME("store/asyncStore.pec")

    def testDeleteRecords(self):
        self.compareResourceEME("store/deleteRecords.pec")

    def testFetchAnd(self):
        self.compareResourceEME("store/fetchAnd.pec")

    def testFetchBoolean(self):
        self.compareResourceEME("store/fetchBoolean.pec")

    def testFetchNotBoolean(self):
        self.compareResourceEME("store/fetchNotBoolean.pec")

    def testFetchOr(self):
        self.compareResourceEME("store/fetchOr.pec")

    def testFlush(self):
        self.compareResourceEME("store/flush.pec")

    def testListRecords(self):
        self.compareResourceEME("store/listRecords.pec")

    def testManyRecords(self):
        self.compareResourceEME("store/manyRecords.pec")

    def testManyUntypedRecords(self):
        self.compareResourceEME("store/manyUntypedRecords.pec")

    def testSimpleRecord(self):
        self.compareResourceEME("store/simpleRecord.pec")

    def testSlicedRecords(self):
        self.compareResourceEME("store/slicedRecords.pec")

    def testSortedRecords(self):
        self.compareResourceEME("store/sortedRecords.pec")

    def testSubRecord(self):
        self.compareResourceEME("store/subRecord.pec")

    def testUntypedRecord(self):
        self.compareResourceEME("store/untypedRecord.pec")


