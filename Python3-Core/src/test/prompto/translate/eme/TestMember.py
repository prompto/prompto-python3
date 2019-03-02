from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestMember(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMemberAttribute(self):
        self.compareResourceEME("member/memberAttribute.pec")


