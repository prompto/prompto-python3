from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestMutability(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testImmutable(self):
        self.checkOutput("mutability/immutable.poc")

    def testMutable(self):
        self.checkOutput("mutability/mutable.poc")


