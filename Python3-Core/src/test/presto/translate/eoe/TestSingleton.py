from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestSingleton(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAttribute(self):
        self.compareResourceEOE("singleton/attribute.pec")

    def testMember(self):
        self.compareResourceEOE("singleton/member.pec")


