from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestTuples(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMultiAssignment(self):
        self.compareResourceEOE("tuples/multiAssignment.e")

    def testSingleAssignment(self):
        self.compareResourceEOE("tuples/singleAssignment.e")

    def testTupleElement(self):
        self.compareResourceEOE("tuples/tupleElement.e")


