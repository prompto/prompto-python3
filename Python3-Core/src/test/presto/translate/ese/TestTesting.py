from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestTesting(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnd(self):
        self.compareResourceESE("testing/and.pec")

    def testContains(self):
        self.compareResourceESE("testing/contains.pec")

    def testGreater(self):
        self.compareResourceESE("testing/greater.pec")

    def testMethod(self):
        self.compareResourceESE("testing/method.pec")

    def testNegative(self):
        self.compareResourceESE("testing/negative.pec")

    def testNegativeError(self):
        self.compareResourceESE("testing/negativeError.pec")

    def testNot(self):
        self.compareResourceESE("testing/not.pec")

    def testOr(self):
        self.compareResourceESE("testing/or.pec")

    def testPositive(self):
        self.compareResourceESE("testing/positive.pec")

    def testPositiveError(self):
        self.compareResourceESE("testing/positiveError.pec")


