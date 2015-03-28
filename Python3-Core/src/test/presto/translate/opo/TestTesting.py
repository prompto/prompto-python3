from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestTesting(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnd(self):
        self.compareResourceOPO("testing/and.o")

    def testContains(self):
        self.compareResourceOPO("testing/contains.o")

    def testGreater(self):
        self.compareResourceOPO("testing/greater.o")

    def testMethod(self):
        self.compareResourceOPO("testing/method.o")

    def testNegative(self):
        self.compareResourceOPO("testing/negative.o")

    def testNegativeError(self):
        self.compareResourceOPO("testing/negativeError.o")

    def testNot(self):
        self.compareResourceOPO("testing/not.o")

    def testOr(self):
        self.compareResourceOPO("testing/or.o")

    def testPositive(self):
        self.compareResourceOPO("testing/positive.o")

    def testPositiveError(self):
        self.compareResourceOPO("testing/positiveError.o")


