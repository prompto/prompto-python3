from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestMult(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMultCharacter(self):
        self.compareResourceESE("mult/multCharacter.pec")

    def testMultDecimal(self):
        self.compareResourceESE("mult/multDecimal.pec")

    def testMultInteger(self):
        self.compareResourceESE("mult/multInteger.pec")

    def testMultList(self):
        self.compareResourceESE("mult/multList.pec")

    def testMultPeriod(self):
        self.compareResourceESE("mult/multPeriod.pec")

    def testMultText(self):
        self.compareResourceESE("mult/multText.pec")


