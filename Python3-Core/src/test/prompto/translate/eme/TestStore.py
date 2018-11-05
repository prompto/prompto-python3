from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestStore(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAsyncFetch(self):
        self.compareResourceEME("store/asyncFetch.pec")

    def testAsyncStore(self):
        self.compareResourceEME("store/asyncStore.pec")

    def testDeleteRecords(self):
        self.compareResourceEME("store/deleteRecords.pec")

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


