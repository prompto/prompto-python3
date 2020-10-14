from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestIterate(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testForEachCategoryList(self):
        self.compareResourceEME("iterate/forEachCategoryList.pec")

    def testForEachExpression(self):
        self.compareResourceEME("iterate/forEachExpression.pec")

    def testForEachIntegerList(self):
        self.compareResourceEME("iterate/forEachIntegerList.pec")

    def testForEachIntegerSet(self):
        self.compareResourceEME("iterate/forEachIntegerSet.pec")


