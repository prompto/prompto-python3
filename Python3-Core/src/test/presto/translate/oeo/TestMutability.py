from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestMutability(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testImmutable(self):
        self.compareResourceOEO("mutability/immutable.poc")

    def testImmutableArgument(self):
        self.compareResourceOEO("mutability/immutableArgument.poc")

    def testImmutableMember(self):
        self.compareResourceOEO("mutability/immutableMember.poc")

    def testMutable(self):
        self.compareResourceOEO("mutability/mutable.poc")

    def testMutableArgument(self):
        self.compareResourceOEO("mutability/mutableArgument.poc")

    def testMutableMember(self):
        self.compareResourceOEO("mutability/mutableMember.poc")


