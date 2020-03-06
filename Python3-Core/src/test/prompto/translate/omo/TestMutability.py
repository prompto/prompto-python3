from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestMutability(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testImmutable(self):
        self.compareResourceOMO("mutability/immutable.poc")

    def testImmutableArgument(self):
        self.compareResourceOMO("mutability/immutableArgument.poc")

    def testImmutableDict(self):
        self.compareResourceOMO("mutability/immutableDict.poc")

    def testImmutableList(self):
        self.compareResourceOMO("mutability/immutableList.poc")

    def testImmutableMember(self):
        self.compareResourceOMO("mutability/immutableMember.poc")

    def testImmutableTuple(self):
        self.compareResourceOMO("mutability/immutableTuple.poc")

    def testMutable(self):
        self.compareResourceOMO("mutability/mutable.poc")

    def testMutableArgument(self):
        self.compareResourceOMO("mutability/mutableArgument.poc")

    def testMutableDict(self):
        self.compareResourceOMO("mutability/mutableDict.poc")

    def testMutableList(self):
        self.compareResourceOMO("mutability/mutableList.poc")

    def testMutableTuple(self):
        self.compareResourceOMO("mutability/mutableTuple.poc")


