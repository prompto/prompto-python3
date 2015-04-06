from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestTesting(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnd(self):
        self.compareResourceEOE("testing/and.pec")

    def testContains(self):
        self.compareResourceEOE("testing/contains.pec")

    def testGreater(self):
        self.compareResourceEOE("testing/greater.pec")

    def testMethod(self):
        self.compareResourceEOE("testing/method.pec")

    def testNegative(self):
        self.compareResourceEOE("testing/negative.pec")

    def testNegativeError(self):
        self.compareResourceEOE("testing/negativeError.pec")

    def testNot(self):
        self.compareResourceEOE("testing/not.pec")

    def testOr(self):
        self.compareResourceEOE("testing/or.pec")

    def testPositive(self):
        self.compareResourceEOE("testing/positive.pec")

    def testPositiveError(self):
        self.compareResourceEOE("testing/positiveError.pec")


