from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestTuples(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMultiAssignment(self):
        self.compareResourceEPE("tuples/multiAssignment.e")

    def testSingleAssignment(self):
        self.compareResourceEPE("tuples/singleAssignment.e")

    def testTupleElement(self):
        self.compareResourceEPE("tuples/tupleElement.e")


