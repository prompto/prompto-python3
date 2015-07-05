# generated: 2015-07-05T23:01:01.811
from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestForward(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testForward(self):
        self.compareResourceESE("forward/forward.pec")


