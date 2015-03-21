from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestLess(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testLtCharacter(self):
        self.compareResourceEPE("less/ltCharacter.e")

    def testLtDate(self):
        self.compareResourceEPE("less/ltDate.e")

    def testLtDateTime(self):
        self.compareResourceEPE("less/ltDateTime.e")

    def testLtDecimal(self):
        self.compareResourceEPE("less/ltDecimal.e")

    def testLteCharacter(self):
        self.compareResourceEPE("less/lteCharacter.e")

    def testLteDate(self):
        self.compareResourceEPE("less/lteDate.e")

    def testLteDateTime(self):
        self.compareResourceEPE("less/lteDateTime.e")

    def testLteDecimal(self):
        self.compareResourceEPE("less/lteDecimal.e")

    def testLteInteger(self):
        self.compareResourceEPE("less/lteInteger.e")

    def testLteText(self):
        self.compareResourceEPE("less/lteText.e")

    def testLteTime(self):
        self.compareResourceEPE("less/lteTime.e")

    def testLtInteger(self):
        self.compareResourceEPE("less/ltInteger.e")

    def testLtText(self):
        self.compareResourceEPE("less/ltText.e")

    def testLtTime(self):
        self.compareResourceEPE("less/ltTime.e")


