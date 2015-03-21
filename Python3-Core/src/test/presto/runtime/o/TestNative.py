from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out

class TestNative(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
        Out.init()
    
    def tearDown(self):
        Out.restore()

    def testCategory(self):
        self.checkOutput("native/category.o")

    def testMethod(self):
        self.checkOutput("native/method.o")

    def testReturnBooleanLiteral(self):
        self.checkOutput("native/returnBooleanLiteral.o")

    def testReturnBooleanObject(self):
        self.checkOutput("native/returnBooleanObject.o")

    def testReturnBooleanValue(self):
        self.checkOutput("native/returnBooleanValue.o")

    def testReturnCharacterLiteral(self):
        self.checkOutput("native/returnCharacterLiteral.o")

    def testReturnCharacterObject(self):
        self.checkOutput("native/returnCharacterObject.o")

    def testReturnCharacterValue(self):
        self.checkOutput("native/returnCharacterValue.o")

    def testReturnDecimalLiteral(self):
        self.checkOutput("native/returnDecimalLiteral.o")

    def testReturnIntegerLiteral(self):
        self.checkOutput("native/returnIntegerLiteral.o")

    def testReturnIntegerObject(self):
        self.checkOutput("native/returnIntegerObject.o")

    def testReturnIntegerValue(self):
        self.checkOutput("native/returnIntegerValue.o")

    def testReturnLongObject(self):
        self.checkOutput("native/returnLongObject.o")

    def testReturnLongValue(self):
        self.checkOutput("native/returnLongValue.o")

    def testReturnStringLiteral(self):
        self.checkOutput("native/returnStringLiteral.o")


