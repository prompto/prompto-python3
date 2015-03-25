from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestTesting(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testNegative(self):
        self.checkOutput("testing/negative.e")

    def testNegativeError(self):
        self.checkOutput("testing/negativeError.e")

    def testPositive(self):
        self.checkOutput("testing/positive.e")

    def testPositiveError(self):
        self.checkOutput("testing/positiveError.e")


