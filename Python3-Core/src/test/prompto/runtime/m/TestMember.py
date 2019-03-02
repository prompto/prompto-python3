from prompto.parser.m.BaseMParserTest import BaseMParserTest
from prompto.runtime.utils.Out import Out

class TestMember(BaseMParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testMemberAttribute(self):
        self.checkOutput("member/memberAttribute.pmc")


