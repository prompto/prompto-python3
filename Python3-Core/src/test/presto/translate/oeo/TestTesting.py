from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestTesting(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnd(self):
        self.compareResourceOEO("testing/and.o")

    def testContains(self):
        self.compareResourceOEO("testing/contains.o")

    def testGreater(self):
        self.compareResourceOEO("testing/greater.o")

    def testMethod(self):
        self.compareResourceOEO("testing/method.o")

    def testNegative(self):
        self.compareResourceOEO("testing/negative.o")

    def testNegativeError(self):
        self.compareResourceOEO("testing/negativeError.o")

    def testNot(self):
        self.compareResourceOEO("testing/not.o")

    def testOr(self):
        self.compareResourceOEO("testing/or.o")

    def testPositive(self):
        self.compareResourceOEO("testing/positive.o")

    def testPositiveError(self):
        self.compareResourceOEO("testing/positiveError.o")


