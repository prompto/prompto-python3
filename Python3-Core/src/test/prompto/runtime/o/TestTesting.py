from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestTesting(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAnd(self):
        self.checkOutput("testing/and.poc")

    def testContains(self):
        self.checkOutput("testing/contains.poc")

    def testGreater(self):
        self.checkOutput("testing/greater.poc")

    def testMethod(self):
        self.checkOutput("testing/method.poc")

    def testNegative(self):
        self.checkOutput("testing/negative.poc")

    def testNegativeError(self):
        self.checkOutput("testing/negativeError.poc")

    def testNot(self):
        self.checkOutput("testing/not.poc")

    def testOr(self):
        self.checkOutput("testing/or.poc")

    def testPositive(self):
        self.checkOutput("testing/positive.poc")

    def testPositiveError(self):
        self.checkOutput("testing/positiveError.poc")


