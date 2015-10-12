from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestMult(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testMultCharacter(self):
        self.checkOutput("mult/multCharacter.poc")

    def testMultDecimal(self):
        self.checkOutput("mult/multDecimal.poc")

    def testMultInteger(self):
        self.checkOutput("mult/multInteger.poc")

    def testMultList(self):
        self.checkOutput("mult/multList.poc")

    def testMultPeriod(self):
        self.checkOutput("mult/multPeriod.poc")

    def testMultText(self):
        self.checkOutput("mult/multText.poc")


