from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestTuples(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMultiAssignment(self):
        self.compareResourceOMO("tuples/multiAssignment.poc")

    def testSingleAssignment(self):
        self.compareResourceOMO("tuples/singleAssignment.poc")

    def testTupleElement(self):
        self.compareResourceOMO("tuples/tupleElement.poc")


