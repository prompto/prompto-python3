from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestSubtract(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSubDate(self):
        self.checkOutput("subtract/subDate.poc")

    def testSubDateTime(self):
        self.checkOutput("subtract/subDateTime.poc")

    def testSubDecimal(self):
        self.checkOutput("subtract/subDecimal.poc")

    def testSubInteger(self):
        self.checkOutput("subtract/subInteger.poc")

    def testSubList(self):
        self.checkOutput("subtract/subList.poc")

    def testSubPeriod(self):
        self.checkOutput("subtract/subPeriod.poc")

    def testSubSet(self):
        self.checkOutput("subtract/subSet.poc")

    def testSubTime(self):
        self.checkOutput("subtract/subTime.poc")


