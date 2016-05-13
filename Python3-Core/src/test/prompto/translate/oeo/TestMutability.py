from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestMutability(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testImmutable(self):
        self.compareResourceOEO("mutability/immutable.poc")

    def testImmutableArgument(self):
        self.compareResourceOEO("mutability/immutableArgument.poc")

    def testImmutableDict(self):
        self.compareResourceOEO("mutability/immutableDict.poc")

    def testImmutableList(self):
        self.compareResourceOEO("mutability/immutableList.poc")

    def testImmutableMember(self):
        self.compareResourceOEO("mutability/immutableMember.poc")

    def testImmutableTuple(self):
        self.compareResourceOEO("mutability/immutableTuple.poc")

    def testMutable(self):
        self.compareResourceOEO("mutability/mutable.poc")

    def testMutableArgument(self):
        self.compareResourceOEO("mutability/mutableArgument.poc")

    def testMutableDict(self):
        self.compareResourceOEO("mutability/mutableDict.poc")

    def testMutableList(self):
        self.compareResourceOEO("mutability/mutableList.poc")

    def testMutableMember(self):
        self.compareResourceOEO("mutability/mutableMember.poc")

    def testMutableTuple(self):
        self.compareResourceOEO("mutability/mutableTuple.poc")


