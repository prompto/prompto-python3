from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestMutability(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testImmutable(self):
        self.checkOutput("mutability/immutable.pec")

    def testMutable(self):
        self.checkOutput("mutability/mutable.pec")


