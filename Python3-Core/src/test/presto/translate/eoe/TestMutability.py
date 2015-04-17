from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestMutability(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testImmutable(self):
        self.compareResourceEOE("mutability/immutable.pec")

    def testMutable(self):
        self.compareResourceEOE("mutability/mutable.pec")


