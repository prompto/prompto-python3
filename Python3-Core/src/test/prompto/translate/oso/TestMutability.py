from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestMutability(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testImmutable(self):
        self.compareResourceOSO("mutability/immutable.poc")

    def testImmutableArgument(self):
        self.compareResourceOSO("mutability/immutableArgument.poc")

    def testImmutableDict(self):
        self.compareResourceOSO("mutability/immutableDict.poc")

    def testImmutableList(self):
        self.compareResourceOSO("mutability/immutableList.poc")

    def testImmutableMember(self):
        self.compareResourceOSO("mutability/immutableMember.poc")

    def testImmutableTuple(self):
        self.compareResourceOSO("mutability/immutableTuple.poc")

    def testMutable(self):
        self.compareResourceOSO("mutability/mutable.poc")

    def testMutableArgument(self):
        self.compareResourceOSO("mutability/mutableArgument.poc")

    def testMutableDict(self):
        self.compareResourceOSO("mutability/mutableDict.poc")

    def testMutableList(self):
        self.compareResourceOSO("mutability/mutableList.poc")

    def testMutableMember(self):
        self.compareResourceOSO("mutability/mutableMember.poc")

    def testMutableTuple(self):
        self.compareResourceOSO("mutability/mutableTuple.poc")


