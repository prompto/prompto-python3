from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestSingleton(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAttribute(self):
        self.compareResourceOMO("singleton/attribute.poc")

    def testMember(self):
        self.compareResourceOMO("singleton/member.poc")


