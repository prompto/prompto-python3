from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestLess(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testLtCharacter(self):
        self.compareResourceOPO("less/ltCharacter.o")

    def testLtDate(self):
        self.compareResourceOPO("less/ltDate.o")

    def testLtDateTime(self):
        self.compareResourceOPO("less/ltDateTime.o")

    def testLtDecimal(self):
        self.compareResourceOPO("less/ltDecimal.o")

    def testLteCharacter(self):
        self.compareResourceOPO("less/lteCharacter.o")

    def testLteDate(self):
        self.compareResourceOPO("less/lteDate.o")

    def testLteDateTime(self):
        self.compareResourceOPO("less/lteDateTime.o")

    def testLteDecimal(self):
        self.compareResourceOPO("less/lteDecimal.o")

    def testLteInteger(self):
        self.compareResourceOPO("less/lteInteger.o")

    def testLteText(self):
        self.compareResourceOPO("less/lteText.o")

    def testLteTime(self):
        self.compareResourceOPO("less/lteTime.o")

    def testLtInteger(self):
        self.compareResourceOPO("less/ltInteger.o")

    def testLtText(self):
        self.compareResourceOPO("less/ltText.o")

    def testLtTime(self):
        self.compareResourceOPO("less/ltTime.o")


