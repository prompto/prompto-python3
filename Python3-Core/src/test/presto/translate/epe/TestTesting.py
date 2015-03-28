from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestTesting(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnd(self):
        self.compareResourceEPE("testing/and.e")

    def testContains(self):
        self.compareResourceEPE("testing/contains.e")

    def testGreater(self):
        self.compareResourceEPE("testing/greater.e")

    def testMethod(self):
        self.compareResourceEPE("testing/method.e")

    def testNegative(self):
        self.compareResourceEPE("testing/negative.e")

    def testNegativeError(self):
        self.compareResourceEPE("testing/negativeError.e")

    def testNot(self):
        self.compareResourceEPE("testing/not.e")

    def testOr(self):
        self.compareResourceEPE("testing/or.e")

    def testPositive(self):
        self.compareResourceEPE("testing/positive.e")

    def testPositiveError(self):
        self.compareResourceEPE("testing/positiveError.e")


