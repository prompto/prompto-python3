from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestMutability(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testImmutable(self):
        self.compareResourceESE("mutability/immutable.pec")

    def testImmutableMember(self):
        self.compareResourceESE("mutability/immutableMember.pec")

    def testMutable(self):
        self.compareResourceESE("mutability/mutable.pec")

    def testMutableMember(self):
        self.compareResourceESE("mutability/mutableMember.pec")


