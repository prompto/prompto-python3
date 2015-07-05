# generated: 2015-07-05T23:01:01.814
from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestForward(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testForward(self):
        self.compareResourceOSO("forward/forward.poc")


