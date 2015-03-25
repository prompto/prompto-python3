from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestTesting(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testNegative(self):
        self.compareResourceOEO("testing/negative.o")

    def testNegativeError(self):
        self.compareResourceOEO("testing/negativeError.o")

    def testPositive(self):
        self.compareResourceOEO("testing/positive.o")

    def testPositiveError(self):
        self.compareResourceOEO("testing/positiveError.o")


