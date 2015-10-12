from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestForward(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testForward(self):
        self.compareResourceOEO("forward/forward.poc")


