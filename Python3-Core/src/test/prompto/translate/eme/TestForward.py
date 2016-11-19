from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestForward(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testForward(self):
        self.compareResourceEME("forward/forward.pec")


