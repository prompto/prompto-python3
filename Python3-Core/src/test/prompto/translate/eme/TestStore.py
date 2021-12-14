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

    def testAuditDelete(self):
        self.compareResourceEME("store/auditDelete.pec")

    def testAuditInsert(self):
        self.compareResourceEME("store/auditInsert.pec")

    def testAuditMany(self):
        self.compareResourceEME("store/auditMany.pec")

    def testAuditMatching(self):
        self.compareResourceEME("store/auditMatching.pec")

    def testAuditUpdate(self):
        self.compareResourceEME("store/auditUpdate.pec")

    def testDeleteAudit(self):
        self.compareResourceEME("store/deleteAudit.pec")

    def testDeleteMeta(self):
        self.compareResourceEME("store/deleteMeta.pec")

    def testDeleteRecords(self):
        self.compareResourceEME("store/deleteRecords.pec")

    def testFetchAnd(self):
        self.compareResourceEME("store/fetchAnd.pec")

    def testFetchBoolean(self):
        self.compareResourceEME("store/fetchBoolean.pec")

    def testFetchContains(self):
        self.compareResourceEME("store/fetchContains.pec")

    def testFetchGreater(self):
        self.compareResourceEME("store/fetchGreater.pec")

    def testFetchGreaterEqual(self):
        self.compareResourceEME("store/fetchGreaterEqual.pec")

    def testFetchHas(self):
        self.compareResourceEME("store/fetchHas.pec")

    def testFetchIn(self):
        self.compareResourceEME("store/fetchIn.pec")

    def testFetchInclude(self):
        self.compareResourceEME("store/fetchInclude.pec")

    def testFetchLesser(self):
        self.compareResourceEME("store/fetchLesser.pec")

    def testFetchLesserEqual(self):
        self.compareResourceEME("store/fetchLesserEqual.pec")

    def testFetchNotBoolean(self):
        self.compareResourceEME("store/fetchNotBoolean.pec")

    def testFetchNotContains(self):
        self.compareResourceEME("store/fetchNotContains.pec")

    def testFetchNotHas(self):
        self.compareResourceEME("store/fetchNotHas.pec")

    def testFetchNotIn(self):
        self.compareResourceEME("store/fetchNotIn.pec")

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


