from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestLess(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testLtCharacter(self):
        self.compareResourceOEO("less/ltCharacter.o")

    def testLtDate(self):
        self.compareResourceOEO("less/ltDate.o")

    def testLtDateTime(self):
        self.compareResourceOEO("less/ltDateTime.o")

    def testLtDecimal(self):
        self.compareResourceOEO("less/ltDecimal.o")

    def testLteCharacter(self):
        self.compareResourceOEO("less/lteCharacter.o")

    def testLteDate(self):
        self.compareResourceOEO("less/lteDate.o")

    def testLteDateTime(self):
        self.compareResourceOEO("less/lteDateTime.o")

    def testLteDecimal(self):
        self.compareResourceOEO("less/lteDecimal.o")

    def testLteInteger(self):
        self.compareResourceOEO("less/lteInteger.o")

    def testLteText(self):
        self.compareResourceOEO("less/lteText.o")

    def testLteTime(self):
        self.compareResourceOEO("less/lteTime.o")

    def testLtInteger(self):
        self.compareResourceOEO("less/ltInteger.o")

    def testLtText(self):
        self.compareResourceOEO("less/ltText.o")

    def testLtTime(self):
        self.compareResourceOEO("less/ltTime.o")


