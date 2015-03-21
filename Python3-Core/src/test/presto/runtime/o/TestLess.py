from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestLess(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testLtCharacter(self):
        self.checkOutput("less/ltCharacter.o")

    def testLtDate(self):
        self.checkOutput("less/ltDate.o")

    def testLtDateTime(self):
        self.checkOutput("less/ltDateTime.o")

    def testLtDecimal(self):
        self.checkOutput("less/ltDecimal.o")

    def testLteCharacter(self):
        self.checkOutput("less/lteCharacter.o")

    def testLteDate(self):
        self.checkOutput("less/lteDate.o")

    def testLteDateTime(self):
        self.checkOutput("less/lteDateTime.o")

    def testLteDecimal(self):
        self.checkOutput("less/lteDecimal.o")

    def testLteInteger(self):
        self.checkOutput("less/lteInteger.o")

    def testLteText(self):
        self.checkOutput("less/lteText.o")

    def testLteTime(self):
        self.checkOutput("less/lteTime.o")

    def testLtInteger(self):
        self.checkOutput("less/ltInteger.o")

    def testLtText(self):
        self.checkOutput("less/ltText.o")

    def testLtTime(self):
        self.checkOutput("less/ltTime.o")


