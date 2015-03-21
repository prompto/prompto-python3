from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestMult(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testMultCharacter(self):
        self.checkOutput("mult/multCharacter.o")

    def testMultDecimal(self):
        self.checkOutput("mult/multDecimal.o")

    def testMultInteger(self):
        self.checkOutput("mult/multInteger.o")

    def testMultList(self):
        self.checkOutput("mult/multList.o")

    def testMultPeriod(self):
        self.checkOutput("mult/multPeriod.o")

    def testMultText(self):
        self.checkOutput("mult/multText.o")


