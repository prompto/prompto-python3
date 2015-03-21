from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestMinus(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMinusDecimal(self):
        self.compareResourceEOE("minus/minusDecimal.e")

    def testMinusInteger(self):
        self.compareResourceEOE("minus/minusInteger.e")

    def testMinusPeriod(self):
        self.compareResourceEOE("minus/minusPeriod.e")


