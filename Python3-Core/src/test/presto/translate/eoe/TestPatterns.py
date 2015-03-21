from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestPatterns(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testIntegerEnumeration(self):
        self.compareResourceEOE("patterns/integerEnumeration.e")

    def testIntegerPattern(self):
        self.compareResourceEOE("patterns/integerPattern.e")

    def testNegativeIntegerRange(self):
        self.compareResourceEOE("patterns/negativeIntegerRange.e")

    def testPositiveIntegerRange(self):
        self.compareResourceEOE("patterns/positiveIntegerRange.e")

    def testTextEnumeration(self):
        self.compareResourceEOE("patterns/textEnumeration.e")

    def testTextPattern(self):
        self.compareResourceEOE("patterns/textPattern.e")


