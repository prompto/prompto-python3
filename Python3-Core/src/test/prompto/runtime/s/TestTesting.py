from prompto.parser.s.BaseSParserTest import BaseSParserTest
from prompto.runtime.utils.Out import Out

class TestTesting(BaseSParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAnd(self):
        self.checkOutput("testing/and.psc")

    def testContains(self):
        self.checkOutput("testing/contains.psc")

    def testGreater(self):
        self.checkOutput("testing/greater.psc")

    def testMethod(self):
        self.checkOutput("testing/method.psc")

    def testNegative(self):
        self.checkOutput("testing/negative.psc")

    def testNegativeError(self):
        self.checkOutput("testing/negativeError.psc")

    def testNot(self):
        self.checkOutput("testing/not.psc")

    def testOr(self):
        self.checkOutput("testing/or.psc")

    def testPositive(self):
        self.checkOutput("testing/positive.psc")

    def testPositiveError(self):
        self.checkOutput("testing/positiveError.psc")


