from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestLess(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testLtCharacter(self):
        self.checkOutput("less/ltCharacter.pec")

    def testLtDate(self):
        self.checkOutput("less/ltDate.pec")

    def testLtDateTime(self):
        self.checkOutput("less/ltDateTime.pec")

    def testLtDecimal(self):
        self.checkOutput("less/ltDecimal.pec")

    def testLteCharacter(self):
        self.checkOutput("less/lteCharacter.pec")

    def testLteDate(self):
        self.checkOutput("less/lteDate.pec")

    def testLteDateTime(self):
        self.checkOutput("less/lteDateTime.pec")

    def testLteDecimal(self):
        self.checkOutput("less/lteDecimal.pec")

    def testLteInteger(self):
        self.checkOutput("less/lteInteger.pec")

    def testLteText(self):
        self.checkOutput("less/lteText.pec")

    def testLteTime(self):
        self.checkOutput("less/lteTime.pec")

    def testLtInteger(self):
        self.checkOutput("less/ltInteger.pec")

    def testLtText(self):
        self.checkOutput("less/ltText.pec")

    def testLtTime(self):
        self.checkOutput("less/ltTime.pec")

    def testLtVersion(self):
        self.checkOutput("less/ltVersion.pec")


