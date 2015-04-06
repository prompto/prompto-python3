from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestMinus(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMinusDecimal(self):
        self.compareResourceOEO("minus/minusDecimal.poc")

    def testMinusInteger(self):
        self.compareResourceOEO("minus/minusInteger.poc")

    def testMinusPeriod(self):
        self.compareResourceOEO("minus/minusPeriod.poc")


