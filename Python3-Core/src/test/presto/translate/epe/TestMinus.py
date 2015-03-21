from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestMinus(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMinusDecimal(self):
        self.compareResourceEPE("minus/minusDecimal.e")

    def testMinusInteger(self):
        self.compareResourceEPE("minus/minusInteger.e")

    def testMinusPeriod(self):
        self.compareResourceEPE("minus/minusPeriod.e")


