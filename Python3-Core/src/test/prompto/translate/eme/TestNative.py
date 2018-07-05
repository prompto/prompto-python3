from prompto.parser.e.BaseEParserTest import BaseEParserTest

class TestNative(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAnyId(self):
        self.compareResourceEME("native/anyId.pec")

    def testAnyText(self):
        self.compareResourceEME("native/anyText.pec")

    def testAttribute(self):
        self.compareResourceEME("native/attribute.pec")

    def testCategory(self):
        self.compareResourceEME("native/category.pec")

    def testCategoryReturn(self):
        self.compareResourceEME("native/categoryReturn.pec")

    def testMethod(self):
        self.compareResourceEME("native/method.pec")

    def testNow(self):
        self.compareResourceEME("native/now.pec")

    def testPrinter(self):
        self.compareResourceEME("native/printer.pec")

    def testReturn(self):
        self.compareResourceEME("native/return.pec")


