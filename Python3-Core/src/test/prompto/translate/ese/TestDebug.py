# generated: 2015-07-05T23:01:01.766
from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestDebug(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testStack(self):
        self.compareResourceESE("debug/stack.pec")


