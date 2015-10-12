from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestSub(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSubDate(self):
        self.checkOutput("sub/subDate.pec")

    def testSubDateTime(self):
        self.checkOutput("sub/subDateTime.pec")

    def testSubDecimal(self):
        self.checkOutput("sub/subDecimal.pec")

    def testSubInteger(self):
        self.checkOutput("sub/subInteger.pec")

    def testSubPeriod(self):
        self.checkOutput("sub/subPeriod.pec")

    def testSubTime(self):
        self.checkOutput("sub/subTime.pec")


