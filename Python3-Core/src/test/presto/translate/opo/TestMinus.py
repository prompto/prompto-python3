from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestMinus(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMinusDecimal(self):
        self.compareResourceOPO("minus/minusDecimal.o")

    def testMinusInteger(self):
        self.compareResourceOPO("minus/minusInteger.o")

    def testMinusPeriod(self):
        self.compareResourceOPO("minus/minusPeriod.o")


