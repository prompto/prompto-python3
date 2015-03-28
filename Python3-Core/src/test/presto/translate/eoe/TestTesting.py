from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestTesting(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnd(self):
        self.compareResourceEOE("testing/and.e")

    def testContains(self):
        self.compareResourceEOE("testing/contains.e")

    def testGreater(self):
        self.compareResourceEOE("testing/greater.e")

    def testMethod(self):
        self.compareResourceEOE("testing/method.e")

    def testNegative(self):
        self.compareResourceEOE("testing/negative.e")

    def testNegativeError(self):
        self.compareResourceEOE("testing/negativeError.e")

    def testNot(self):
        self.compareResourceEOE("testing/not.e")

    def testOr(self):
        self.compareResourceEOE("testing/or.e")

    def testPositive(self):
        self.compareResourceEOE("testing/positive.e")

    def testPositiveError(self):
        self.compareResourceEOE("testing/positiveError.e")


