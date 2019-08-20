from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestTypes(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testLiteral(self):
        self.compareResourceOMO("types/literal.poc")


