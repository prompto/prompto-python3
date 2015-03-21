from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestLess(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testLtCharacter(self):
        self.checkOutput("less/ltCharacter.e")

    def testLtDate(self):
        self.checkOutput("less/ltDate.e")

    def testLtDateTime(self):
        self.checkOutput("less/ltDateTime.e")

    def testLtDecimal(self):
        self.checkOutput("less/ltDecimal.e")

    def testLteCharacter(self):
        self.checkOutput("less/lteCharacter.e")

    def testLteDate(self):
        self.checkOutput("less/lteDate.e")

    def testLteDateTime(self):
        self.checkOutput("less/lteDateTime.e")

    def testLteDecimal(self):
        self.checkOutput("less/lteDecimal.e")

    def testLteInteger(self):
        self.checkOutput("less/lteInteger.e")

    def testLteText(self):
        self.checkOutput("less/lteText.e")

    def testLteTime(self):
        self.checkOutput("less/lteTime.e")

    def testLtInteger(self):
        self.checkOutput("less/ltInteger.e")

    def testLtText(self):
        self.checkOutput("less/ltText.e")

    def testLtTime(self):
        self.checkOutput("less/ltTime.e")


