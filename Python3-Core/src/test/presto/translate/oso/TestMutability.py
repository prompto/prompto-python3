from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestMutability(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testImmutable(self):
        self.compareResourceOSO("mutability/immutable.poc")

    def testImmutableArgument(self):
        self.compareResourceOSO("mutability/immutableArgument.poc")

    def testImmutableMember(self):
        self.compareResourceOSO("mutability/immutableMember.poc")

    def testMutable(self):
        self.compareResourceOSO("mutability/mutable.poc")

    def testMutableArgument(self):
        self.compareResourceOSO("mutability/mutableArgument.poc")

    def testMutableMember(self):
        self.compareResourceOSO("mutability/mutableMember.poc")


