from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestTuples(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testMultiAssignment(self):
        self.checkOutput("tuples/multiAssignment.pec")

    def testSingleAssignment(self):
        self.checkOutput("tuples/singleAssignment.pec")

    def testTupleElement(self):
        self.checkOutput("tuples/tupleElement.pec")


