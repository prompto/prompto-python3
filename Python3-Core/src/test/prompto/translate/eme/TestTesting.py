from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestTesting(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnd(self):
        self.compareResourceEME("testing/and.pec")

    def testContains(self):
        self.compareResourceEME("testing/contains.pec")

    def testGreater(self):
        self.compareResourceEME("testing/greater.pec")

    def testMethod(self):
        self.compareResourceEME("testing/method.pec")

    def testNegative(self):
        self.compareResourceEME("testing/negative.pec")

    def testNegativeError(self):
        self.compareResourceEME("testing/negativeError.pec")

    def testNot(self):
        self.compareResourceEME("testing/not.pec")

    def testOr(self):
        self.compareResourceEME("testing/or.pec")

    def testPositive(self):
        self.compareResourceEME("testing/positive.pec")

    def testPositiveError(self):
        self.compareResourceEME("testing/positiveError.pec")


