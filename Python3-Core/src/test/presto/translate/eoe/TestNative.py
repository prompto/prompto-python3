from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestNative(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategory(self):
        self.compareResourceEOE("native/category.pec")

    def testMethod(self):
        self.compareResourceEOE("native/method.pec")

    def testPrint(self):
        self.compareResourceEOE("native/print.pec")

    def testReturn(self):
        self.compareResourceEOE("native/return.pec")


