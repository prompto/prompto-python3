from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestTuples(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMultiAssignment(self):
        self.compareResourceOEO("tuples/multiAssignment.poc")

    def testSingleAssignment(self):
        self.compareResourceOEO("tuples/singleAssignment.poc")

    def testTupleElement(self):
        self.compareResourceOEO("tuples/tupleElement.poc")


