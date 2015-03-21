from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestPatterns(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testIntegerEnumeration(self):
        self.compareResourceEPE("patterns/integerEnumeration.e")

    def testIntegerPattern(self):
        self.compareResourceEPE("patterns/integerPattern.e")

    def testNegativeIntegerRange(self):
        self.compareResourceEPE("patterns/negativeIntegerRange.e")

    def testPositiveIntegerRange(self):
        self.compareResourceEPE("patterns/positiveIntegerRange.e")

    def testTextEnumeration(self):
        self.compareResourceEPE("patterns/textEnumeration.e")

    def testTextPattern(self):
        self.compareResourceEPE("patterns/textPattern.e")


