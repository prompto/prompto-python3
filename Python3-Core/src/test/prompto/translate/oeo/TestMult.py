from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestMult(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMultCharacter(self):
        self.compareResourceOEO("mult/multCharacter.poc")

    def testMultDecimal(self):
        self.compareResourceOEO("mult/multDecimal.poc")

    def testMultInteger(self):
        self.compareResourceOEO("mult/multInteger.poc")

    def testMultList(self):
        self.compareResourceOEO("mult/multList.poc")

    def testMultPeriod(self):
        self.compareResourceOEO("mult/multPeriod.poc")

    def testMultText(self):
        self.compareResourceOEO("mult/multText.poc")


