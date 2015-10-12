from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestLess(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testLtCharacter(self):
        self.checkOutput("less/ltCharacter.poc")

    def testLtDate(self):
        self.checkOutput("less/ltDate.poc")

    def testLtDateTime(self):
        self.checkOutput("less/ltDateTime.poc")

    def testLtDecimal(self):
        self.checkOutput("less/ltDecimal.poc")

    def testLteCharacter(self):
        self.checkOutput("less/lteCharacter.poc")

    def testLteDate(self):
        self.checkOutput("less/lteDate.poc")

    def testLteDateTime(self):
        self.checkOutput("less/lteDateTime.poc")

    def testLteDecimal(self):
        self.checkOutput("less/lteDecimal.poc")

    def testLteInteger(self):
        self.checkOutput("less/lteInteger.poc")

    def testLteText(self):
        self.checkOutput("less/lteText.poc")

    def testLteTime(self):
        self.checkOutput("less/lteTime.poc")

    def testLtInteger(self):
        self.checkOutput("less/ltInteger.poc")

    def testLtText(self):
        self.checkOutput("less/ltText.poc")

    def testLtTime(self):
        self.checkOutput("less/ltTime.poc")


