from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestPatterns(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testIntegerEnumeration(self):
        self.compareResourceOEO("patterns/integerEnumeration.o")

    def testIntegerPattern(self):
        self.compareResourceOEO("patterns/integerPattern.o")

    def testNegativeIntegerRange(self):
        self.compareResourceOEO("patterns/negativeIntegerRange.o")

    def testPositiveIntegerRange(self):
        self.compareResourceOEO("patterns/positiveIntegerRange.o")

    def testTextEnumeration(self):
        self.compareResourceOEO("patterns/textEnumeration.o")

    def testTextPattern(self):
        self.compareResourceOEO("patterns/textPattern.o")


