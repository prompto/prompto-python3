from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestPatterns(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testIntegerEnumeration(self):
        self.compareResourceOEO("patterns/integerEnumeration.poc")

    def testIntegerPattern(self):
        self.compareResourceOEO("patterns/integerPattern.poc")

    def testNegativeIntegerRange(self):
        self.compareResourceOEO("patterns/negativeIntegerRange.poc")

    def testPositiveIntegerRange(self):
        self.compareResourceOEO("patterns/positiveIntegerRange.poc")

    def testTextEnumeration(self):
        self.compareResourceOEO("patterns/textEnumeration.poc")

    def testTextPattern(self):
        self.compareResourceOEO("patterns/textPattern.poc")


