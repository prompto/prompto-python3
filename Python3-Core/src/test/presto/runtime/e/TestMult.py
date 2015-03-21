from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestMult(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testMultCharacter(self):
        self.checkOutput("mult/multCharacter.e")

    def testMultDecimal(self):
        self.checkOutput("mult/multDecimal.e")

    def testMultInteger(self):
        self.checkOutput("mult/multInteger.e")

    def testMultList(self):
        self.checkOutput("mult/multList.e")

    def testMultPeriod(self):
        self.checkOutput("mult/multPeriod.e")

    def testMultText(self):
        self.checkOutput("mult/multText.e")


