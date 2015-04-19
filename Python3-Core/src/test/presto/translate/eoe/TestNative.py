from presto.parser.e.BaseEParserTest import BaseEParserTest

class TestNative(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testAttribute(self):
        self.compareResourceEOE("native/attribute.pec")

    def testCategory(self):
        self.compareResourceEOE("native/category.pec")

    def testMethod(self):
        self.compareResourceEOE("native/method.pec")

    def testPrinter(self):
        self.compareResourceEOE("native/printer.pec")

    def testReturn(self):
        self.compareResourceEOE("native/return.pec")


