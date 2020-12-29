from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestMutability(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testDowncastMutable(self):
        self.checkOutput("mutability/downcastMutable.poc")

    def testImmutable(self):
        self.checkOutput("mutability/immutable.poc")

    def testImmutableArgument(self):
        self.checkOutput("mutability/immutableArgument.poc")

    def testImmutableDict(self):
        self.checkOutput("mutability/immutableDict.poc")

    def testImmutableList(self):
        self.checkOutput("mutability/immutableList.poc")

    def testImmutableMember(self):
        self.checkOutput("mutability/immutableMember.poc")

    def testImmutableTuple(self):
        self.checkOutput("mutability/immutableTuple.poc")

    def testMutable(self):
        self.checkOutput("mutability/mutable.poc")

    def testMutableArgument(self):
        self.checkOutput("mutability/mutableArgument.poc")

    def testMutableDict(self):
        self.checkOutput("mutability/mutableDict.poc")

    def testMutableList(self):
        self.checkOutput("mutability/mutableList.poc")

    def testMutableTuple(self):
        self.checkOutput("mutability/mutableTuple.poc")


