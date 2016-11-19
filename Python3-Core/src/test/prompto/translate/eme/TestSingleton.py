from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSingleton(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAttribute(self):
        self.compareResourceEME("singleton/attribute.pec")

    def testMember(self):
        self.compareResourceEME("singleton/member.pec")


