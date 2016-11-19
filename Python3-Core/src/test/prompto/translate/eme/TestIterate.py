from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestIterate(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testForEachCategoryList(self):
        self.compareResourceEME("iterate/forEachCategoryList.pec")

    def testForEachIntegerList(self):
        self.compareResourceEME("iterate/forEachIntegerList.pec")


