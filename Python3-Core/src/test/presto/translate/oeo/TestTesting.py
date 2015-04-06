from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestTesting(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnd(self):
        self.compareResourceOEO("testing/and.poc")

    def testContains(self):
        self.compareResourceOEO("testing/contains.poc")

    def testGreater(self):
        self.compareResourceOEO("testing/greater.poc")

    def testMethod(self):
        self.compareResourceOEO("testing/method.poc")

    def testNegative(self):
        self.compareResourceOEO("testing/negative.poc")

    def testNegativeError(self):
        self.compareResourceOEO("testing/negativeError.poc")

    def testNot(self):
        self.compareResourceOEO("testing/not.poc")

    def testOr(self):
        self.compareResourceOEO("testing/or.poc")

    def testPositive(self):
        self.compareResourceOEO("testing/positive.poc")

    def testPositiveError(self):
        self.compareResourceOEO("testing/positiveError.poc")


