from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestPatterns(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testIntegerEnumeration(self):
        self.compareResourceOSO("patterns/integerEnumeration.poc")

    def testIntegerPattern(self):
        self.compareResourceOSO("patterns/integerPattern.poc")

    def testNegativeIntegerRange(self):
        self.compareResourceOSO("patterns/negativeIntegerRange.poc")

    def testPositiveIntegerRange(self):
        self.compareResourceOSO("patterns/positiveIntegerRange.poc")

    def testTextEnumeration(self):
        self.compareResourceOSO("patterns/textEnumeration.poc")

    def testTextPattern(self):
        self.compareResourceOSO("patterns/textPattern.poc")


