from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestMinus(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMinusDecimal(self):
        self.compareResourceOEO("minus/minusDecimal.o")

    def testMinusInteger(self):
        self.compareResourceOEO("minus/minusInteger.o")

    def testMinusPeriod(self):
        self.compareResourceOEO("minus/minusPeriod.o")


