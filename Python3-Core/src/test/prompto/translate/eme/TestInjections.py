from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestInjections(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testExpressionInjection(self):
        self.compareResourceEME("injections/expressionInjection.pec")


