from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestLess(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testLtCharacter(self):
        self.compareResourceOEO("less/ltCharacter.poc")

    def testLtDate(self):
        self.compareResourceOEO("less/ltDate.poc")

    def testLtDateTime(self):
        self.compareResourceOEO("less/ltDateTime.poc")

    def testLtDecimal(self):
        self.compareResourceOEO("less/ltDecimal.poc")

    def testLteCharacter(self):
        self.compareResourceOEO("less/lteCharacter.poc")

    def testLteDate(self):
        self.compareResourceOEO("less/lteDate.poc")

    def testLteDateTime(self):
        self.compareResourceOEO("less/lteDateTime.poc")

    def testLteDecimal(self):
        self.compareResourceOEO("less/lteDecimal.poc")

    def testLteInteger(self):
        self.compareResourceOEO("less/lteInteger.poc")

    def testLteText(self):
        self.compareResourceOEO("less/lteText.poc")

    def testLteTime(self):
        self.compareResourceOEO("less/lteTime.poc")

    def testLtInteger(self):
        self.compareResourceOEO("less/ltInteger.poc")

    def testLtText(self):
        self.compareResourceOEO("less/ltText.poc")

    def testLtTime(self):
        self.compareResourceOEO("less/ltTime.poc")

    def testLtVersion(self):
        self.compareResourceOEO("less/ltVersion.poc")


