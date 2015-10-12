from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestTuples(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testMultiAssignment(self):
        self.checkOutput("tuples/multiAssignment.poc")

    def testSingleAssignment(self):
        self.checkOutput("tuples/singleAssignment.poc")

    def testTupleElement(self):
        self.checkOutput("tuples/tupleElement.poc")


