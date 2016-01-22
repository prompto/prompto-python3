from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestStore(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testManyRecords(self):
        self.compareResourceESE("store/manyRecords.pec")

    def testSimpleRecord(self):
        self.compareResourceESE("store/simpleRecord.pec")

    def testSlicedRecords(self):
        self.compareResourceESE("store/slicedRecords.pec")

    def testSortedRecords(self):
        self.compareResourceESE("store/sortedRecords.pec")

    def testSubRecord(self):
        self.compareResourceESE("store/subRecord.pec")

