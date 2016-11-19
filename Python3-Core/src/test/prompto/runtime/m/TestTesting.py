from prompto.parser.m.BaseMParserTest import BaseMParserTest
from prompto.runtime.utils.Out import Out

class TestTesting(BaseMParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAnd(self):
        self.checkOutput("testing/and.pmc")

    def testContains(self):
        self.checkOutput("testing/contains.pmc")

    def testGreater(self):
        self.checkOutput("testing/greater.pmc")

    def testMethod(self):
        self.checkOutput("testing/method.pmc")

    def testNegative(self):
        self.checkOutput("testing/negative.pmc")

    def testNegativeError(self):
        self.checkOutput("testing/negativeError.pmc")

    def testNot(self):
        self.checkOutput("testing/not.pmc")

    def testOr(self):
        self.checkOutput("testing/or.pmc")

    def testPositive(self):
        self.checkOutput("testing/positive.pmc")

    def testPositiveError(self):
        self.checkOutput("testing/positiveError.pmc")


