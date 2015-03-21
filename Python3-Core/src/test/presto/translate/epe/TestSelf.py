from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestSelf(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSelfAsParameter(self):
        self.compareResourceEPE("self/selfAsParameter.e")

    def testSelfMember(self):
        self.compareResourceEPE("self/selfMember.e")


