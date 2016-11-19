from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestTuples(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMultiAssignment(self):
        self.compareResourceEME("tuples/multiAssignment.pec")

    def testSingleAssignment(self):
        self.compareResourceEME("tuples/singleAssignment.pec")

    def testTupleElement(self):
        self.compareResourceEME("tuples/tupleElement.pec")


