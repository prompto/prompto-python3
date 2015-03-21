from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestTuples(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMultiAssignment(self):
        self.compareResourceOPO("tuples/multiAssignment.o")

    def testSingleAssignment(self):
        self.compareResourceOPO("tuples/singleAssignment.o")

    def testTupleElement(self):
        self.compareResourceOPO("tuples/tupleElement.o")


