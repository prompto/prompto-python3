from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestMult(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMultCharacter(self):
        self.compareResourceOMO("mult/multCharacter.poc")

    def testMultDecimal(self):
        self.compareResourceOMO("mult/multDecimal.poc")

    def testMultInteger(self):
        self.compareResourceOMO("mult/multInteger.poc")

    def testMultList(self):
        self.compareResourceOMO("mult/multList.poc")

    def testMultPeriod(self):
        self.compareResourceOMO("mult/multPeriod.poc")

    def testMultText(self):
        self.compareResourceOMO("mult/multText.poc")


