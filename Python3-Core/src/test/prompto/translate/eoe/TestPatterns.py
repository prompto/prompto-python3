from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestPatterns(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testIntegerEnumeration(self):
        self.compareResourceEOE("patterns/integerEnumeration.pec")

    def testIntegerPattern(self):
        self.compareResourceEOE("patterns/integerPattern.pec")

    def testNegativeIntegerRange(self):
        self.compareResourceEOE("patterns/negativeIntegerRange.pec")

    def testPositiveIntegerRange(self):
        self.compareResourceEOE("patterns/positiveIntegerRange.pec")

    def testTextEnumeration(self):
        self.compareResourceEOE("patterns/textEnumeration.pec")

    def testTextPattern(self):
        self.compareResourceEOE("patterns/textPattern.pec")


