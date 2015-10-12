from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestTesting(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAnd(self):
        self.checkOutput("testing/and.pec")

    def testContains(self):
        self.checkOutput("testing/contains.pec")

    def testGreater(self):
        self.checkOutput("testing/greater.pec")

    def testMethod(self):
        self.checkOutput("testing/method.pec")

    def testNegative(self):
        self.checkOutput("testing/negative.pec")

    def testNegativeError(self):
        self.checkOutput("testing/negativeError.pec")

    def testNot(self):
        self.checkOutput("testing/not.pec")

    def testOr(self):
        self.checkOutput("testing/or.pec")

    def testPositive(self):
        self.checkOutput("testing/positive.pec")

    def testPositiveError(self):
        self.checkOutput("testing/positiveError.pec")


