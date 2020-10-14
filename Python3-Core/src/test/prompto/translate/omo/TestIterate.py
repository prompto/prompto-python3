from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestIterate(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testForEachExpression(self):
        self.compareResourceOMO("iterate/forEachExpression.poc")

    def testForEachIntegerList(self):
        self.compareResourceOMO("iterate/forEachIntegerList.poc")

    def testForEachIntegerRange(self):
        self.compareResourceOMO("iterate/forEachIntegerRange.poc")

    def testForEachIntegerSet(self):
        self.compareResourceOMO("iterate/forEachIntegerSet.poc")


