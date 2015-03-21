from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestPatterns(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testIntegerEnumeration(self):
        self.compareResourceOPO("patterns/integerEnumeration.o")

    def testIntegerPattern(self):
        self.compareResourceOPO("patterns/integerPattern.o")

    def testNegativeIntegerRange(self):
        self.compareResourceOPO("patterns/negativeIntegerRange.o")

    def testPositiveIntegerRange(self):
        self.compareResourceOPO("patterns/positiveIntegerRange.o")

    def testTextEnumeration(self):
        self.compareResourceOPO("patterns/textEnumeration.o")

    def testTextPattern(self):
        self.compareResourceOPO("patterns/textPattern.o")


