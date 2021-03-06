from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.runtime.utils.Out import Out

class TestNative(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAnyId(self):
        self.checkOutput("native/anyId.pec")

    def testAnyText(self):
        self.checkOutput("native/anyText.pec")

    def testAttribute(self):
        self.checkOutput("native/attribute.pec")

    def testCategory(self):
        self.checkOutput("native/category.pec")

    def testCategoryReturn(self):
        self.checkOutput("native/categoryReturn.pec")

    def testMethod(self):
        self.checkOutput("native/method.pec")

    def testNow(self):
        self.checkOutput("native/now.pec")

    def testPrinter(self):
        self.checkOutput("native/printer.pec")


