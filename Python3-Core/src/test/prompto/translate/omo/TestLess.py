from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestLess(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testLtCharacter(self):
        self.compareResourceOMO("less/ltCharacter.poc")

    def testLtDate(self):
        self.compareResourceOMO("less/ltDate.poc")

    def testLtDateTime(self):
        self.compareResourceOMO("less/ltDateTime.poc")

    def testLtDecimal(self):
        self.compareResourceOMO("less/ltDecimal.poc")

    def testLtInteger(self):
        self.compareResourceOMO("less/ltInteger.poc")

    def testLtText(self):
        self.compareResourceOMO("less/ltText.poc")

    def testLtTime(self):
        self.compareResourceOMO("less/ltTime.poc")

    def testLtVersion(self):
        self.compareResourceOMO("less/ltVersion.poc")

    def testLteCharacter(self):
        self.compareResourceOMO("less/lteCharacter.poc")

    def testLteDate(self):
        self.compareResourceOMO("less/lteDate.poc")

    def testLteDateTime(self):
        self.compareResourceOMO("less/lteDateTime.poc")

    def testLteDecimal(self):
        self.compareResourceOMO("less/lteDecimal.poc")

    def testLteInteger(self):
        self.compareResourceOMO("less/lteInteger.poc")

    def testLteText(self):
        self.compareResourceOMO("less/lteText.poc")

    def testLteTime(self):
        self.compareResourceOMO("less/lteTime.poc")


