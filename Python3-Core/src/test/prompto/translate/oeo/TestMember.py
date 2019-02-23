from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestMember(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMemberAttribute(self):
        self.compareResourceOEO("member/memberAttribute.poc")


