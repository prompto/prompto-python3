from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestLess(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testLtCharacter(self):
        self.compareResourceEME("less/ltCharacter.pec")

    def testLtDate(self):
        self.compareResourceEME("less/ltDate.pec")

    def testLtDateTime(self):
        self.compareResourceEME("less/ltDateTime.pec")

    def testLtDecimal(self):
        self.compareResourceEME("less/ltDecimal.pec")

    def testLteCharacter(self):
        self.compareResourceEME("less/lteCharacter.pec")

    def testLteDate(self):
        self.compareResourceEME("less/lteDate.pec")

    def testLteDateTime(self):
        self.compareResourceEME("less/lteDateTime.pec")

    def testLteDecimal(self):
        self.compareResourceEME("less/lteDecimal.pec")

    def testLteInteger(self):
        self.compareResourceEME("less/lteInteger.pec")

    def testLteText(self):
        self.compareResourceEME("less/lteText.pec")

    def testLteTime(self):
        self.compareResourceEME("less/lteTime.pec")

    def testLtInteger(self):
        self.compareResourceEME("less/ltInteger.pec")

    def testLtText(self):
        self.compareResourceEME("less/ltText.pec")

    def testLtTime(self):
        self.compareResourceEME("less/ltTime.pec")

    def testLtVersion(self):
        self.compareResourceEME("less/ltVersion.pec")


