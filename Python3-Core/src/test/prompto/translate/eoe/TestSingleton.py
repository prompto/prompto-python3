from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSingleton(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAttribute(self):
        self.compareResourceEOE("singleton/attribute.pec")

    def testInitialize(self):
        self.compareResourceEOE("singleton/initialize.pec")

    def testInternal(self):
        self.compareResourceEOE("singleton/internal.pec")

    def testMember(self):
        self.compareResourceEOE("singleton/member.pec")


