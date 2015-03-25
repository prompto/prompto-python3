from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestTesting(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testNegative(self):
        self.compareResourceEPE("testing/negative.e")

    def testNegativeError(self):
        self.compareResourceEPE("testing/negativeError.e")

    def testPositive(self):
        self.compareResourceEPE("testing/positive.e")

    def testPositiveError(self):
        self.compareResourceEPE("testing/positiveError.e")


