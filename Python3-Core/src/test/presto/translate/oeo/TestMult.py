from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestMult(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMultCharacter(self):
        self.compareResourceOEO("mult/multCharacter.o")

    def testMultDecimal(self):
        self.compareResourceOEO("mult/multDecimal.o")

    def testMultInteger(self):
        self.compareResourceOEO("mult/multInteger.o")

    def testMultList(self):
        self.compareResourceOEO("mult/multList.o")

    def testMultPeriod(self):
        self.compareResourceOEO("mult/multPeriod.o")

    def testMultText(self):
        self.compareResourceOEO("mult/multText.o")


