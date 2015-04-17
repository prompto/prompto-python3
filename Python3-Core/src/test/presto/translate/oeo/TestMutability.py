from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestMutability(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testImmutable(self):
        self.compareResourceOEO("mutability/immutable.poc")

    def testImmutableMember(self):
        self.compareResourceOEO("mutability/immutableMember.poc")

    def testMutable(self):
        self.compareResourceOEO("mutability/mutable.poc")

    def testMutableMember(self):
        self.compareResourceOEO("mutability/mutableMember.poc")


