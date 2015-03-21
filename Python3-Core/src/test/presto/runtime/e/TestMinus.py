from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestMinus(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testMinusDecimal(self):
        self.checkOutput("minus/minusDecimal.e")

    def testMinusInteger(self):
        self.checkOutput("minus/minusInteger.e")

    def testMinusPeriod(self):
        self.checkOutput("minus/minusPeriod.e")


