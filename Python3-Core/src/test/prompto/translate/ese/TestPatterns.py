from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestPatterns(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testIntegerEnumeration(self):
        self.compareResourceESE("patterns/integerEnumeration.pec")

    def testIntegerPattern(self):
        self.compareResourceESE("patterns/integerPattern.pec")

    def testNegativeIntegerRange(self):
        self.compareResourceESE("patterns/negativeIntegerRange.pec")

    def testPositiveIntegerRange(self):
        self.compareResourceESE("patterns/positiveIntegerRange.pec")

    def testTextEnumeration(self):
        self.compareResourceESE("patterns/textEnumeration.pec")

    def testTextPattern(self):
        self.compareResourceESE("patterns/textPattern.pec")


