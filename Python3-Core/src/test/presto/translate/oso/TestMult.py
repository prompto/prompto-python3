from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestMult(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMultCharacter(self):
        self.compareResourceOSO("mult/multCharacter.poc")

    def testMultDecimal(self):
        self.compareResourceOSO("mult/multDecimal.poc")

    def testMultInteger(self):
        self.compareResourceOSO("mult/multInteger.poc")

    def testMultList(self):
        self.compareResourceOSO("mult/multList.poc")

    def testMultPeriod(self):
        self.compareResourceOSO("mult/multPeriod.poc")

    def testMultText(self):
        self.compareResourceOSO("mult/multText.poc")


