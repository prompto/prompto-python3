from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestInjections(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testExpressionInjection(self):
        self.compareResourceOMO("injections/expressionInjection.poc")


