from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestMutability(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testImmutable(self):
        self.compareResourceEME("mutability/immutable.pec")

    def testImmutableArgument(self):
        self.compareResourceEME("mutability/immutableArgument.pec")

    def testImmutableDict(self):
        self.compareResourceEME("mutability/immutableDict.pec")

    def testImmutableList(self):
        self.compareResourceEME("mutability/immutableList.pec")

    def testImmutableMember(self):
        self.compareResourceEME("mutability/immutableMember.pec")

    def testImmutableTuple(self):
        self.compareResourceEME("mutability/immutableTuple.pec")

    def testMutable(self):
        self.compareResourceEME("mutability/mutable.pec")

    def testMutableArgument(self):
        self.compareResourceEME("mutability/mutableArgument.pec")

    def testMutableChild(self):
        self.compareResourceEME("mutability/mutableChild.pec")

    def testMutableDict(self):
        self.compareResourceEME("mutability/mutableDict.pec")

    def testMutableInstance(self):
        self.compareResourceEME("mutability/mutableInstance.pec")

    def testMutableList(self):
        self.compareResourceEME("mutability/mutableList.pec")

    def testMutableTuple(self):
        self.compareResourceEME("mutability/mutableTuple.pec")


