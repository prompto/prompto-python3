from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestMinus(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMinusDecimal(self):
        self.compareResourceESE("minus/minusDecimal.pec")

    def testMinusInteger(self):
        self.compareResourceESE("minus/minusInteger.pec")

    def testMinusPeriod(self):
        self.compareResourceESE("minus/minusPeriod.pec")


