# generated: 2015-07-05T23:01:01.826
from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestInjections(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testExpressionInjection(self):
        self.compareResourceESE("injections/expressionInjection.pec")


