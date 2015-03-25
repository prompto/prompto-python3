from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestTesting(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testNegative(self):
        self.compareResourceOPO("testing/negative.o")

    def testNegativeError(self):
        self.compareResourceOPO("testing/negativeError.o")

    def testPositive(self):
        self.compareResourceOPO("testing/positive.o")

    def testPositiveError(self):
        self.compareResourceOPO("testing/positiveError.o")


