from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestStore(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAsyncFetch(self):
        self.checkOutput("store/asyncFetch.pec")

    def testAsyncStore(self):
        self.checkOutput("store/asyncStore.pec")

    def testDeleteRecords(self):
        self.checkOutput("store/deleteRecords.pec")

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


