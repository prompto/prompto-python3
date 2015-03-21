from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestMult(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMultCharacter(self):
        self.compareResourceEPE("mult/multCharacter.e")

    def testMultDecimal(self):
        self.compareResourceEPE("mult/multDecimal.e")

    def testMultInteger(self):
        self.compareResourceEPE("mult/multInteger.e")

    def testMultList(self):
        self.compareResourceEPE("mult/multList.e")

    def testMultPeriod(self):
        self.compareResourceEPE("mult/multPeriod.e")

    def testMultText(self):
        self.compareResourceEPE("mult/multText.e")


