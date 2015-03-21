from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestSub(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSubDate(self):
        self.checkOutput("sub/subDate.e")

    def testSubDateTime(self):
        self.checkOutput("sub/subDateTime.e")

    def testSubDecimal(self):
        self.checkOutput("sub/subDecimal.e")

    def testSubInteger(self):
        self.checkOutput("sub/subInteger.e")

    def testSubPeriod(self):
        self.checkOutput("sub/subPeriod.e")

    def testSubTime(self):
        self.checkOutput("sub/subTime.e")


