from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestNative(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategory(self):
        self.compareResourceESE("native/category.pec")

    def testMethod(self):
        self.compareResourceESE("native/method.pec")

    def testPrint(self):
        self.compareResourceESE("native/print.pec")

    def testReturn(self):
        self.compareResourceESE("native/return.pec")


