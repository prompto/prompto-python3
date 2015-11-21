from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestIterate(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testForEachIntegerList(self):
        self.compareResourceOEO("iterate/forEachIntegerList.poc")


