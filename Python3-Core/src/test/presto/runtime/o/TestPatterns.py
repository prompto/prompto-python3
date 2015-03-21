from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestPatterns(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testIntegerEnumeration(self):
        self.checkOutput("patterns/integerEnumeration.o")

    def testIntegerPattern(self):
        self.checkOutput("patterns/integerPattern.o")

    def testNegativeIntegerRange(self):
        self.checkOutput("patterns/negativeIntegerRange.o")

    def testPositiveIntegerRange(self):
        self.checkOutput("patterns/positiveIntegerRange.o")

    def testTextEnumeration(self):
        self.checkOutput("patterns/textEnumeration.o")

    def testTextPattern(self):
        self.checkOutput("patterns/textPattern.o")


