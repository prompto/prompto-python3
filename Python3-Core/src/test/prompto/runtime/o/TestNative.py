from prompto.parser.o.BaseOParserTest import BaseOParserTest
from prompto.runtime.utils.Out import Out

class TestNative(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testCategory(self):
        self.checkOutput("native/category.poc")

    def testMethod(self):
        self.checkOutput("native/method.poc")

    def testReturnBooleanLiteral(self):
        self.checkOutput("native/returnBooleanLiteral.poc")

    def testReturnBooleanObject(self):
        self.checkOutput("native/returnBooleanObject.poc")

    def testReturnBooleanValue(self):
        self.checkOutput("native/returnBooleanValue.poc")

    def testReturnCharacterLiteral(self):
        self.checkOutput("native/returnCharacterLiteral.poc")

    def testReturnCharacterObject(self):
        self.checkOutput("native/returnCharacterObject.poc")

    def testReturnCharacterValue(self):
        self.checkOutput("native/returnCharacterValue.poc")

    def testReturnDecimalLiteral(self):
        self.checkOutput("native/returnDecimalLiteral.poc")

    def testReturnIntegerLiteral(self):
        self.checkOutput("native/returnIntegerLiteral.poc")

    def testReturnIntegerObject(self):
        self.checkOutput("native/returnIntegerObject.poc")

    def testReturnIntegerValue(self):
        self.checkOutput("native/returnIntegerValue.poc")

    def testReturnLongObject(self):
        self.checkOutput("native/returnLongObject.poc")

    def testReturnLongValue(self):
        self.checkOutput("native/returnLongValue.poc")

    def testReturnStringLiteral(self):
        self.checkOutput("native/returnStringLiteral.poc")


