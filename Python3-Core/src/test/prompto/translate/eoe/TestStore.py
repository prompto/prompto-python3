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

    def testAuditDelete(self):
        self.compareResourceEOE("store/auditDelete.pec")

    def testAuditInsert(self):
        self.compareResourceEOE("store/auditInsert.pec")

    def testAuditMany(self):
        self.compareResourceEOE("store/auditMany.pec")

    def testAuditMatching(self):
        self.compareResourceEOE("store/auditMatching.pec")

    def testAuditUpdate(self):
        self.compareResourceEOE("store/auditUpdate.pec")

    def testDeleteAudit(self):
        self.compareResourceEOE("store/deleteAudit.pec")

    def testDeleteMeta(self):
        self.compareResourceEOE("store/deleteMeta.pec")

    def testDeleteRecords(self):
        self.compareResourceEOE("store/deleteRecords.pec")

    def testFetchAnd(self):
        self.compareResourceEOE("store/fetchAnd.pec")

    def testFetchBoolean(self):
        self.compareResourceEOE("store/fetchBoolean.pec")

    def testFetchContains(self):
        self.compareResourceEOE("store/fetchContains.pec")

    def testFetchGreater(self):
        self.compareResourceEOE("store/fetchGreater.pec")

    def testFetchGreaterEqual(self):
        self.compareResourceEOE("store/fetchGreaterEqual.pec")

    def testFetchHas(self):
        self.compareResourceEOE("store/fetchHas.pec")

    def testFetchIn(self):
        self.compareResourceEOE("store/fetchIn.pec")

    def testFetchLesser(self):
        self.compareResourceEOE("store/fetchLesser.pec")

    def testFetchLesserEqual(self):
        self.compareResourceEOE("store/fetchLesserEqual.pec")

    def testFetchNotBoolean(self):
        self.compareResourceEOE("store/fetchNotBoolean.pec")

    def testFetchNotContains(self):
        self.compareResourceEOE("store/fetchNotContains.pec")

    def testFetchNotHas(self):
        self.compareResourceEOE("store/fetchNotHas.pec")

    def testFetchNotIn(self):
        self.compareResourceEOE("store/fetchNotIn.pec")

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


