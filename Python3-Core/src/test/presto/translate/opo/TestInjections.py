from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestInjections(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testExpressionInjection(self):
        self.compareResourceOPO("injections/expressionInjection.o")


