# generated: 2015-07-05T23:01:01.924
from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSelf(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSelfAsParameter(self):
        self.compareResourceEOE("self/selfAsParameter.pec")

    def testSelfMember(self):
        self.compareResourceEOE("self/selfMember.pec")


