from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestMinus(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMinusDecimal(self):
        self.compareResourceOSO("minus/minusDecimal.poc")

    def testMinusInteger(self):
        self.compareResourceOSO("minus/minusInteger.poc")

    def testMinusPeriod(self):
        self.compareResourceOSO("minus/minusPeriod.poc")


