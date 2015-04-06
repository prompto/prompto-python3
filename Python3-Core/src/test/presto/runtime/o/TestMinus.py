from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestMinus(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testMinusDecimal(self):
        self.checkOutput("minus/minusDecimal.poc")

    def testMinusInteger(self):
        self.checkOutput("minus/minusInteger.poc")

    def testMinusPeriod(self):
        self.checkOutput("minus/minusPeriod.poc")


