from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestLess(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testLtCharacter(self):
        self.compareResourceEOE("less/ltCharacter.pec")

    def testLtDate(self):
        self.compareResourceEOE("less/ltDate.pec")

    def testLtDateTime(self):
        self.compareResourceEOE("less/ltDateTime.pec")

    def testLtDecimal(self):
        self.compareResourceEOE("less/ltDecimal.pec")

    def testLteCharacter(self):
        self.compareResourceEOE("less/lteCharacter.pec")

    def testLteDate(self):
        self.compareResourceEOE("less/lteDate.pec")

    def testLteDateTime(self):
        self.compareResourceEOE("less/lteDateTime.pec")

    def testLteDecimal(self):
        self.compareResourceEOE("less/lteDecimal.pec")

    def testLteInteger(self):
        self.compareResourceEOE("less/lteInteger.pec")

    def testLteText(self):
        self.compareResourceEOE("less/lteText.pec")

    def testLteTime(self):
        self.compareResourceEOE("less/lteTime.pec")

    def testLtInteger(self):
        self.compareResourceEOE("less/ltInteger.pec")

    def testLtText(self):
        self.compareResourceEOE("less/ltText.pec")

    def testLtTime(self):
        self.compareResourceEOE("less/ltTime.pec")


