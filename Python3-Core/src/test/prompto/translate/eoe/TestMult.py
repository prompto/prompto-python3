from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestMult(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMultCharacter(self):
        self.compareResourceEOE("mult/multCharacter.pec")

    def testMultDecimal(self):
        self.compareResourceEOE("mult/multDecimal.pec")

    def testMultInteger(self):
        self.compareResourceEOE("mult/multInteger.pec")

    def testMultList(self):
        self.compareResourceEOE("mult/multList.pec")

    def testMultPeriod(self):
        self.compareResourceEOE("mult/multPeriod.pec")

    def testMultText(self):
        self.compareResourceEOE("mult/multText.pec")


