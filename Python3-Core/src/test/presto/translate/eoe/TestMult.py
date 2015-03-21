from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestMult(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testMultCharacter(self):
        self.compareResourceEOE("mult/multCharacter.e")

    def testMultDecimal(self):
        self.compareResourceEOE("mult/multDecimal.e")

    def testMultInteger(self):
        self.compareResourceEOE("mult/multInteger.e")

    def testMultList(self):
        self.compareResourceEOE("mult/multList.e")

    def testMultPeriod(self):
        self.compareResourceEOE("mult/multPeriod.e")

    def testMultText(self):
        self.compareResourceEOE("mult/multText.e")


