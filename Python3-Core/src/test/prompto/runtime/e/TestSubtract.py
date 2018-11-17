from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestSubtract(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testSubDate(self):
        self.checkOutput("subtract/subDate.pec")

    def testSubDateTime(self):
        self.checkOutput("subtract/subDateTime.pec")

    def testSubDecimal(self):
        self.checkOutput("subtract/subDecimal.pec")

    def testSubDecimalEnum(self):
        self.checkOutput("subtract/subDecimalEnum.pec")

    def testSubInteger(self):
        self.checkOutput("subtract/subInteger.pec")

    def testSubIntegerEnum(self):
        self.checkOutput("subtract/subIntegerEnum.pec")

    def testSubList(self):
        self.checkOutput("subtract/subList.pec")

    def testSubPeriod(self):
        self.checkOutput("subtract/subPeriod.pec")

    def testSubSet(self):
        self.checkOutput("subtract/subSet.pec")

    def testSubTime(self):
        self.checkOutput("subtract/subTime.pec")


