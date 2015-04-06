from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestLess(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testLtCharacter(self):
        self.compareResourceOSO("less/ltCharacter.poc")

    def testLtDate(self):
        self.compareResourceOSO("less/ltDate.poc")

    def testLtDateTime(self):
        self.compareResourceOSO("less/ltDateTime.poc")

    def testLtDecimal(self):
        self.compareResourceOSO("less/ltDecimal.poc")

    def testLteCharacter(self):
        self.compareResourceOSO("less/lteCharacter.poc")

    def testLteDate(self):
        self.compareResourceOSO("less/lteDate.poc")

    def testLteDateTime(self):
        self.compareResourceOSO("less/lteDateTime.poc")

    def testLteDecimal(self):
        self.compareResourceOSO("less/lteDecimal.poc")

    def testLteInteger(self):
        self.compareResourceOSO("less/lteInteger.poc")

    def testLteText(self):
        self.compareResourceOSO("less/lteText.poc")

    def testLteTime(self):
        self.compareResourceOSO("less/lteTime.poc")

    def testLtInteger(self):
        self.compareResourceOSO("less/ltInteger.poc")

    def testLtText(self):
        self.compareResourceOSO("less/ltText.poc")

    def testLtTime(self):
        self.compareResourceOSO("less/ltTime.poc")


