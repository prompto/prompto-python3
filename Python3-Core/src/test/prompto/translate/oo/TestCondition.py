from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestCondition(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testEmbeddedIf(self):
        self.compareResourceOO("condition/embeddedIf.poc")



