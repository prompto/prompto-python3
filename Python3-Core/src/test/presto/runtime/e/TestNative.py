from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.runtime.utils.Out import Out

class TestNative(BaseEParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testAttribute(self):
        self.checkOutput("native/attribute.pec")

    def testCategory(self):
        self.checkOutput("native/category.pec")

    def testMethod(self):
        self.checkOutput("native/method.pec")

    def testPrinter(self):
        self.checkOutput("native/printer.pec")


