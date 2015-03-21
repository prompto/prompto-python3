from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestPatterns(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testIntegerEnumeration(self):
        self.checkOutput("patterns/integerEnumeration.e")

    def testIntegerPattern(self):
        self.checkOutput("patterns/integerPattern.e")

    def testNegativeIntegerRange(self):
        self.checkOutput("patterns/negativeIntegerRange.e")

    def testPositiveIntegerRange(self):
        self.checkOutput("patterns/positiveIntegerRange.e")

    def testTextEnumeration(self):
        self.checkOutput("patterns/textEnumeration.e")

    def testTextPattern(self):
        self.checkOutput("patterns/textPattern.e")


