from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestSingleton(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAttribute(self):
        self.compareResourceEPE("singleton/attribute.e")

    def testMember(self):
        self.compareResourceEPE("singleton/member.e")


