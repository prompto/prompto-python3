from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestSub(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSubDate(self):
        self.checkOutput("sub/subDate.o")

    def testSubDateTime(self):
        self.checkOutput("sub/subDateTime.o")

    def testSubDecimal(self):
        self.checkOutput("sub/subDecimal.o")

    def testSubInteger(self):
        self.checkOutput("sub/subInteger.o")

    def testSubPeriod(self):
        self.checkOutput("sub/subPeriod.o")

    def testSubTime(self):
        self.checkOutput("sub/subTime.o")


