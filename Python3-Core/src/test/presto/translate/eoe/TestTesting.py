from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestTesting(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testNegative(self):
        self.compareResourceEOE("testing/negative.e")

    def testNegativeError(self):
        self.compareResourceEOE("testing/negativeError.e")

    def testPositive(self):
        self.compareResourceEOE("testing/positive.e")

    def testPositiveError(self):
        self.compareResourceEOE("testing/positiveError.e")


