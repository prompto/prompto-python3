from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestPatterns(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testIntegerEnumeration(self):
        self.compareResourceEME("patterns/integerEnumeration.pec")

    def testIntegerPattern(self):
        self.compareResourceEME("patterns/integerPattern.pec")

    def testNegativeIntegerRange(self):
        self.compareResourceEME("patterns/negativeIntegerRange.pec")

    def testPositiveIntegerRange(self):
        self.compareResourceEME("patterns/positiveIntegerRange.pec")

    def testTextEnumeration(self):
        self.compareResourceEME("patterns/textEnumeration.pec")

    def testTextPattern(self):
        self.compareResourceEME("patterns/textPattern.pec")


