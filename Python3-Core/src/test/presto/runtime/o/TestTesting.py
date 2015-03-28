from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestTesting(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAnd(self):
        self.checkOutput("testing/and.o")

    def testContains(self):
        self.checkOutput("testing/contains.o")

    def testGreater(self):
        self.checkOutput("testing/greater.o")

    def testMethod(self):
        self.checkOutput("testing/method.o")

    def testNegative(self):
        self.checkOutput("testing/negative.o")

    def testNegativeError(self):
        self.checkOutput("testing/negativeError.o")

    def testNot(self):
        self.checkOutput("testing/not.o")

    def testOr(self):
        self.checkOutput("testing/or.o")

    def testPositive(self):
        self.checkOutput("testing/positive.o")

    def testPositiveError(self):
        self.checkOutput("testing/positiveError.o")


