# generated: 2015-07-05T23:01:01.829
from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestInjections(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testExpressionInjection(self):
        self.compareResourceOSO("injections/expressionInjection.poc")


