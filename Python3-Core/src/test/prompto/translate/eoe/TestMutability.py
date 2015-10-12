from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestMutability(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testImmutable(self):
        self.compareResourceEOE("mutability/immutable.pec")

    def testImmutableArgument(self):
        self.compareResourceEOE("mutability/immutableArgument.pec")

    def testImmutableMember(self):
        self.compareResourceEOE("mutability/immutableMember.pec")

    def testMutable(self):
        self.compareResourceEOE("mutability/mutable.pec")

    def testMutableArgument(self):
        self.compareResourceEOE("mutability/mutableArgument.pec")

    def testMutableMember(self):
        self.compareResourceEOE("mutability/mutableMember.pec")


