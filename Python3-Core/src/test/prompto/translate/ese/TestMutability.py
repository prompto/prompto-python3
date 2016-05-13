from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestMutability(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testImmutable(self):
        self.compareResourceESE("mutability/immutable.pec")

    def testImmutableArgument(self):
        self.compareResourceESE("mutability/immutableArgument.pec")

    def testImmutableDict(self):
        self.compareResourceESE("mutability/immutableDict.pec")

    def testImmutableList(self):
        self.compareResourceESE("mutability/immutableList.pec")

    def testImmutableMember(self):
        self.compareResourceESE("mutability/immutableMember.pec")

    def testImmutableTuple(self):
        self.compareResourceESE("mutability/immutableTuple.pec")

    def testMutable(self):
        self.compareResourceESE("mutability/mutable.pec")

    def testMutableArgument(self):
        self.compareResourceESE("mutability/mutableArgument.pec")

    def testMutableDict(self):
        self.compareResourceESE("mutability/mutableDict.pec")

    def testMutableList(self):
        self.compareResourceESE("mutability/mutableList.pec")

    def testMutableMember(self):
        self.compareResourceESE("mutability/mutableMember.pec")

    def testMutableTuple(self):
        self.compareResourceESE("mutability/mutableTuple.pec")


