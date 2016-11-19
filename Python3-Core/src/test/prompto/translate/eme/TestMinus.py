from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestMinus(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMinusDecimal(self):
        self.compareResourceEME("minus/minusDecimal.pec")

    def testMinusInteger(self):
        self.compareResourceEME("minus/minusInteger.pec")

    def testMinusPeriod(self):
        self.compareResourceEME("minus/minusPeriod.pec")


