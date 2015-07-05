# generated: 2015-07-05T23:01:01.938
from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSingleton(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAttribute(self):
        self.compareResourceEOE("singleton/attribute.pec")

    def testMember(self):
        self.compareResourceEOE("singleton/member.pec")


