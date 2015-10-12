from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestTuples(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMultiAssignment(self):
        self.compareResourceESE("tuples/multiAssignment.pec")

    def testSingleAssignment(self):
        self.compareResourceESE("tuples/singleAssignment.pec")

    def testTupleElement(self):
        self.compareResourceESE("tuples/tupleElement.pec")


