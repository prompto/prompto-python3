from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestIterate(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testForEachIntegerList(self):
        self.compareResourceESE("iterate/forEachIntegerList.pec")


