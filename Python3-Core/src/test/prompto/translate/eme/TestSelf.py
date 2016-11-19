from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSelf(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSelfAsParameter(self):
        self.compareResourceEME("self/selfAsParameter.pec")

    def testSelfMember(self):
        self.compareResourceEME("self/selfMember.pec")


