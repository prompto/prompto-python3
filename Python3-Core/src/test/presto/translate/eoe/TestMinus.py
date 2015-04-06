from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestMinus(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMinusDecimal(self):
        self.compareResourceEOE("minus/minusDecimal.pec")

    def testMinusInteger(self):
        self.compareResourceEOE("minus/minusInteger.pec")

    def testMinusPeriod(self):
        self.compareResourceEOE("minus/minusPeriod.pec")


