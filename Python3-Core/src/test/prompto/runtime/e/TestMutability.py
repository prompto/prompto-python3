from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestMutability(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testImmutable(self):
        self.checkOutput("mutability/immutable.pec")

    def testImmutableArgument(self):
        self.checkOutput("mutability/immutableArgument.pec")

    def testImmutableDict(self):
        self.checkOutput("mutability/immutableDict.pec")

    def testImmutableList(self):
        self.checkOutput("mutability/immutableList.pec")

    def testImmutableMember(self):
        self.checkOutput("mutability/immutableMember.pec")

    def testImmutableTuple(self):
        self.checkOutput("mutability/immutableTuple.pec")

    def testMutable(self):
        self.checkOutput("mutability/mutable.pec")

    def testMutableArgument(self):
        self.checkOutput("mutability/mutableArgument.pec")

    def testMutableChild(self):
        self.checkOutput("mutability/mutableChild.pec")

    def testMutableDict(self):
        self.checkOutput("mutability/mutableDict.pec")

    def testMutableInstance(self):
        self.checkOutput("mutability/mutableInstance.pec")

    def testMutableList(self):
        self.checkOutput("mutability/mutableList.pec")

    def testMutableMember(self):
        self.checkOutput("mutability/mutableMember.pec")

    def testMutableTuple(self):
        self.checkOutput("mutability/mutableTuple.pec")


