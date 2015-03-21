from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestMult(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMultCharacter(self):
        self.compareResourceOPO("mult/multCharacter.o")

    def testMultDecimal(self):
        self.compareResourceOPO("mult/multDecimal.o")

    def testMultInteger(self):
        self.compareResourceOPO("mult/multInteger.o")

    def testMultList(self):
        self.compareResourceOPO("mult/multList.o")

    def testMultPeriod(self):
        self.compareResourceOPO("mult/multPeriod.o")

    def testMultText(self):
        self.compareResourceOPO("mult/multText.o")


