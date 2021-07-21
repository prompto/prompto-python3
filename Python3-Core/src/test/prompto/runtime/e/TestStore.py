from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestStore(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAsyncFetchMany(self):
        self.checkOutput("store/asyncFetchMany.pec")

    def testAsyncFetchOne(self):
        self.checkOutput("store/asyncFetchOne.pec")

    def testAsyncStore(self):
        self.checkOutput("store/asyncStore.pec")

    def testAuditRecord(self):
        self.checkOutput("store/auditRecord.pec")

    def testDeleteRecords(self):
        self.checkOutput("store/deleteRecords.pec")

    def testFetchAnd(self):
        self.checkOutput("store/fetchAnd.pec")

    def testFetchBoolean(self):
        self.checkOutput("store/fetchBoolean.pec")

    def testFetchContains(self):
        self.checkOutput("store/fetchContains.pec")

    def testFetchGreater(self):
        self.checkOutput("store/fetchGreater.pec")

    def testFetchGreaterEqual(self):
        self.checkOutput("store/fetchGreaterEqual.pec")

    def testFetchHas(self):
        self.checkOutput("store/fetchHas.pec")

    def testFetchIn(self):
        self.checkOutput("store/fetchIn.pec")

    def testFetchLesser(self):
        self.checkOutput("store/fetchLesser.pec")

    def testFetchLesserEqual(self):
        self.checkOutput("store/fetchLesserEqual.pec")

    def testFetchNotBoolean(self):
        self.checkOutput("store/fetchNotBoolean.pec")

    def testFetchNotContains(self):
        self.checkOutput("store/fetchNotContains.pec")

    def testFetchNotHas(self):
        self.checkOutput("store/fetchNotHas.pec")

    def testFetchNotIn(self):
        self.checkOutput("store/fetchNotIn.pec")

    def testFetchOr(self):
        self.checkOutput("store/fetchOr.pec")

    def testFlush(self):
        self.checkOutput("store/flush.pec")

    def testListRecords(self):
        self.checkOutput("store/listRecords.pec")

    def testManyRecords(self):
        self.checkOutput("store/manyRecords.pec")

    def testManyUntypedRecords(self):
        self.checkOutput("store/manyUntypedRecords.pec")

    def testSimpleRecord(self):
        self.checkOutput("store/simpleRecord.pec")

    def testSlicedRecords(self):
        self.checkOutput("store/slicedRecords.pec")

    def testSortedRecords(self):
        self.checkOutput("store/sortedRecords.pec")

    def testSubRecord(self):
        self.checkOutput("store/subRecord.pec")

    def testUntypedRecord(self):
        self.checkOutput("store/untypedRecord.pec")


