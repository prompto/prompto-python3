from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestMutability(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testImmutable(self):
        self.compareResourceEOE("mutability/immutable.pec")

    def testImmutableArgument(self):
        self.compareResourceEOE("mutability/immutableArgument.pec")

    def testImmutableDict(self):
        self.compareResourceEOE("mutability/immutableDict.pec")

    def testImmutableList(self):
        self.compareResourceEOE("mutability/immutableList.pec")

    def testImmutableMember(self):
        self.compareResourceEOE("mutability/immutableMember.pec")

    def testImmutableTuple(self):
        self.compareResourceEOE("mutability/immutableTuple.pec")

    def testMutable(self):
        self.compareResourceEOE("mutability/mutable.pec")

    def testMutableArgument(self):
        self.compareResourceEOE("mutability/mutableArgument.pec")

    def testMutableChild(self):
        self.compareResourceEOE("mutability/mutableChild.pec")

    def testMutableDict(self):
        self.compareResourceEOE("mutability/mutableDict.pec")

    def testMutableInstance(self):
        self.compareResourceEOE("mutability/mutableInstance.pec")

    def testMutableList(self):
        self.compareResourceEOE("mutability/mutableList.pec")

    def testMutableMember(self):
        self.compareResourceEOE("mutability/mutableMember.pec")

    def testMutableTuple(self):
        self.compareResourceEOE("mutability/mutableTuple.pec")


