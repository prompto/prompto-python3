from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestPatterns(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testIntegerEnumeration(self):
        self.checkOutput("patterns/integerEnumeration.pec")

    def testIntegerPattern(self):
        self.checkOutput("patterns/integerPattern.pec")

    def testNegativeIntegerRange(self):
        self.checkOutput("patterns/negativeIntegerRange.pec")

    def testPositiveIntegerRange(self):
        self.checkOutput("patterns/positiveIntegerRange.pec")

    def testTextEnumeration(self):
        self.checkOutput("patterns/textEnumeration.pec")

    def testTextPattern(self):
        self.checkOutput("patterns/textPattern.pec")


