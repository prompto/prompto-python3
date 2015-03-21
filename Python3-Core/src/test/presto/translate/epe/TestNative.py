from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestNative(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategory(self):
        self.compareResourceEPE("native/category.e")

    def testMethod(self):
        self.compareResourceEPE("native/method.e")

    def testReturn(self):
        self.compareResourceEPE("native/return.e")


