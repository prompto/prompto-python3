# generated: 2015-07-05T23:01:01.875
from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestMinus(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMinusDecimal(self):
        self.compareResourceEOE("minus/minusDecimal.pec")

    def testMinusInteger(self):
        self.compareResourceEOE("minus/minusInteger.pec")

    def testMinusPeriod(self):
        self.compareResourceEOE("minus/minusPeriod.pec")


