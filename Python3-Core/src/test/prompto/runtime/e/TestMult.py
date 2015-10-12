from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestMult(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testMultCharacter(self):
        self.checkOutput("mult/multCharacter.pec")

    def testMultDecimal(self):
        self.checkOutput("mult/multDecimal.pec")

    def testMultInteger(self):
        self.checkOutput("mult/multInteger.pec")

    def testMultList(self):
        self.checkOutput("mult/multList.pec")

    def testMultPeriod(self):
        self.checkOutput("mult/multPeriod.pec")

    def testMultText(self):
        self.checkOutput("mult/multText.pec")


