from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestPatterns(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testIntegerEnumeration(self):
        self.compareResourceOMO("patterns/integerEnumeration.poc")

    def testIntegerPattern(self):
        self.compareResourceOMO("patterns/integerPattern.poc")

    def testNegativeIntegerRange(self):
        self.compareResourceOMO("patterns/negativeIntegerRange.poc")

    def testPositiveIntegerRange(self):
        self.compareResourceOMO("patterns/positiveIntegerRange.poc")

    def testTextEnumeration(self):
        self.compareResourceOMO("patterns/textEnumeration.poc")

    def testTextPattern(self):
        self.compareResourceOMO("patterns/textPattern.poc")


