from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestTesting(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnd(self):
        self.compareResourceOSO("testing/and.poc")

    def testContains(self):
        self.compareResourceOSO("testing/contains.poc")

    def testGreater(self):
        self.compareResourceOSO("testing/greater.poc")

    def testMethod(self):
        self.compareResourceOSO("testing/method.poc")

    def testNegative(self):
        self.compareResourceOSO("testing/negative.poc")

    def testNegativeError(self):
        self.compareResourceOSO("testing/negativeError.poc")

    def testNot(self):
        self.compareResourceOSO("testing/not.poc")

    def testOr(self):
        self.compareResourceOSO("testing/or.poc")

    def testPositive(self):
        self.compareResourceOSO("testing/positive.poc")

    def testPositiveError(self):
        self.compareResourceOSO("testing/positiveError.poc")


