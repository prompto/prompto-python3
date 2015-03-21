from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestTuples(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testMultiAssignment(self):
        self.checkOutput("tuples/multiAssignment.o")

    def testSingleAssignment(self):
        self.checkOutput("tuples/singleAssignment.o")

    def testTupleElement(self):
        self.checkOutput("tuples/tupleElement.o")


