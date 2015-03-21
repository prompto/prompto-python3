from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestForward(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testForward(self):
        self.compareResourceEOE("forward/forward.e")


