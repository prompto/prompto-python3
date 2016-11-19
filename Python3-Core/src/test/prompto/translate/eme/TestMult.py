from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestMult(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMultCharacter(self):
        self.compareResourceEME("mult/multCharacter.pec")

    def testMultDecimal(self):
        self.compareResourceEME("mult/multDecimal.pec")

    def testMultInteger(self):
        self.compareResourceEME("mult/multInteger.pec")

    def testMultList(self):
        self.compareResourceEME("mult/multList.pec")

    def testMultPeriod(self):
        self.compareResourceEME("mult/multPeriod.pec")

    def testMultText(self):
        self.compareResourceEME("mult/multText.pec")


