from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestSub(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSubDate(self):
        self.checkOutput("sub/subDate.poc")

    def testSubDateTime(self):
        self.checkOutput("sub/subDateTime.poc")

    def testSubDecimal(self):
        self.checkOutput("sub/subDecimal.poc")

    def testSubInteger(self):
        self.checkOutput("sub/subInteger.poc")

    def testSubPeriod(self):
        self.checkOutput("sub/subPeriod.poc")

    def testSubTime(self):
        self.checkOutput("sub/subTime.poc")


