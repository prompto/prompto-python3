from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestSingleton(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAttribute(self):
        self.checkOutput("singleton/attribute.pec")

    def testConstructor(self):
        self.checkOutput("singleton/constructor.pec")

    def testInternal(self):
        self.checkOutput("singleton/internal.pec")

    def testMember(self):
        self.checkOutput("singleton/member.pec")


