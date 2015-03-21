from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestLess(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testLtCharacter(self):
        self.compareResourceEOE("less/ltCharacter.e")

    def testLtDate(self):
        self.compareResourceEOE("less/ltDate.e")

    def testLtDateTime(self):
        self.compareResourceEOE("less/ltDateTime.e")

    def testLtDecimal(self):
        self.compareResourceEOE("less/ltDecimal.e")

    def testLteCharacter(self):
        self.compareResourceEOE("less/lteCharacter.e")

    def testLteDate(self):
        self.compareResourceEOE("less/lteDate.e")

    def testLteDateTime(self):
        self.compareResourceEOE("less/lteDateTime.e")

    def testLteDecimal(self):
        self.compareResourceEOE("less/lteDecimal.e")

    def testLteInteger(self):
        self.compareResourceEOE("less/lteInteger.e")

    def testLteText(self):
        self.compareResourceEOE("less/lteText.e")

    def testLteTime(self):
        self.compareResourceEOE("less/lteTime.e")

    def testLtInteger(self):
        self.compareResourceEOE("less/ltInteger.e")

    def testLtText(self):
        self.compareResourceEOE("less/ltText.e")

    def testLtTime(self):
        self.compareResourceEOE("less/ltTime.e")


