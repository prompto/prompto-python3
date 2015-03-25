from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestTesting(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testNegative(self):
        self.checkOutput("testing/negative.o")

    def testNegativeError(self):
        self.checkOutput("testing/negativeError.o")

    def testPositive(self):
        self.checkOutput("testing/positive.o")

    def testPositiveError(self):
        self.checkOutput("testing/positiveError.o")


