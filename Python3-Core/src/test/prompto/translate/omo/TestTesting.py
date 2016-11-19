from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestTesting(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnd(self):
        self.compareResourceOMO("testing/and.poc")

    def testContains(self):
        self.compareResourceOMO("testing/contains.poc")

    def testGreater(self):
        self.compareResourceOMO("testing/greater.poc")

    def testMethod(self):
        self.compareResourceOMO("testing/method.poc")

    def testNegative(self):
        self.compareResourceOMO("testing/negative.poc")

    def testNegativeError(self):
        self.compareResourceOMO("testing/negativeError.poc")

    def testNot(self):
        self.compareResourceOMO("testing/not.poc")

    def testOr(self):
        self.compareResourceOMO("testing/or.poc")

    def testPositive(self):
        self.compareResourceOMO("testing/positive.poc")

    def testPositiveError(self):
        self.compareResourceOMO("testing/positiveError.poc")


