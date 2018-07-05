from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestNative(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnyId(self):
        self.compareResourceEOE("native/anyId.pec")

    def testAnyText(self):
        self.compareResourceEOE("native/anyText.pec")

    def testAttribute(self):
        self.compareResourceEOE("native/attribute.pec")

    def testCategory(self):
        self.compareResourceEOE("native/category.pec")

    def testCategoryReturn(self):
        self.compareResourceEOE("native/categoryReturn.pec")

    def testMethod(self):
        self.compareResourceEOE("native/method.pec")

    def testNow(self):
        self.compareResourceEOE("native/now.pec")

    def testPrinter(self):
        self.compareResourceEOE("native/printer.pec")

    def testReturn(self):
        self.compareResourceEOE("native/return.pec")


