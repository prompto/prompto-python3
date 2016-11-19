from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestMinus(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMinusDecimal(self):
        self.compareResourceOMO("minus/minusDecimal.poc")

    def testMinusInteger(self):
        self.compareResourceOMO("minus/minusInteger.poc")

    def testMinusPeriod(self):
        self.compareResourceOMO("minus/minusPeriod.poc")


