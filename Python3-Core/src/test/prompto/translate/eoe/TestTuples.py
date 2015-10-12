from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestTuples(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMultiAssignment(self):
        self.compareResourceEOE("tuples/multiAssignment.pec")

    def testSingleAssignment(self):
        self.compareResourceEOE("tuples/singleAssignment.pec")

    def testTupleElement(self):
        self.compareResourceEOE("tuples/tupleElement.pec")


