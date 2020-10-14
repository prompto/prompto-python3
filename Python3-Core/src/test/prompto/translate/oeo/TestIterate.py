from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestIterate(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testForEachExpression(self):
        self.compareResourceOEO("iterate/forEachExpression.poc")

    def testForEachIntegerList(self):
        self.compareResourceOEO("iterate/forEachIntegerList.poc")

    def testForEachIntegerRange(self):
        self.compareResourceOEO("iterate/forEachIntegerRange.poc")

    def testForEachIntegerSet(self):
        self.compareResourceOEO("iterate/forEachIntegerSet.poc")


