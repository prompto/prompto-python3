# generated: 2015-07-05T23:01:01.979
from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestTuples(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMultiAssignment(self):
        self.compareResourceOSO("tuples/multiAssignment.poc")

    def testSingleAssignment(self):
        self.compareResourceOSO("tuples/singleAssignment.poc")

    def testTupleElement(self):
        self.compareResourceOSO("tuples/tupleElement.poc")


