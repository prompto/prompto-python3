from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestSelf(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testSelfAsParameter(self):
        self.compareResourceEOE("self/selfAsParameter.pec")


