from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestTesting(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAnd(self):
        self.checkOutput("testing/and.e")

    def testContains(self):
        self.checkOutput("testing/contains.e")

    def testGreater(self):
        self.checkOutput("testing/greater.e")

    def testMethod(self):
        self.checkOutput("testing/method.e")

    def testNegative(self):
        self.checkOutput("testing/negative.e")

    def testNegativeError(self):
        self.checkOutput("testing/negativeError.e")

    def testNot(self):
        self.checkOutput("testing/not.e")

    def testOr(self):
        self.checkOutput("testing/or.e")

    def testPositive(self):
        self.checkOutput("testing/positive.e")

    def testPositiveError(self):
        self.checkOutput("testing/positiveError.e")


