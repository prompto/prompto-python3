from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestLess(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testLtCharacter(self):
        self.compareResourceESE("less/ltCharacter.pec")

    def testLtDate(self):
        self.compareResourceESE("less/ltDate.pec")

    def testLtDateTime(self):
        self.compareResourceESE("less/ltDateTime.pec")

    def testLtDecimal(self):
        self.compareResourceESE("less/ltDecimal.pec")

    def testLteCharacter(self):
        self.compareResourceESE("less/lteCharacter.pec")

    def testLteDate(self):
        self.compareResourceESE("less/lteDate.pec")

    def testLteDateTime(self):
        self.compareResourceESE("less/lteDateTime.pec")

    def testLteDecimal(self):
        self.compareResourceESE("less/lteDecimal.pec")

    def testLteInteger(self):
        self.compareResourceESE("less/lteInteger.pec")

    def testLteText(self):
        self.compareResourceESE("less/lteText.pec")

    def testLteTime(self):
        self.compareResourceESE("less/lteTime.pec")

    def testLtInteger(self):
        self.compareResourceESE("less/ltInteger.pec")

    def testLtText(self):
        self.compareResourceESE("less/ltText.pec")

    def testLtTime(self):
        self.compareResourceESE("less/ltTime.pec")


