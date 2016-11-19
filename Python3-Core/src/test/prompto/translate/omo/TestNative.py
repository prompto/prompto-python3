from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestNative(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategory(self):
        self.compareResourceOMO("native/category.poc")

    def testMethod(self):
        self.compareResourceOMO("native/method.poc")

    def testReturn(self):
        self.compareResourceOMO("native/return.poc")

    def testReturnBooleanLiteral(self):
        self.compareResourceOMO("native/returnBooleanLiteral.poc")

    def testReturnBooleanObject(self):
        self.compareResourceOMO("native/returnBooleanObject.poc")

    def testReturnBooleanValue(self):
        self.compareResourceOMO("native/returnBooleanValue.poc")

    def testReturnCharacterLiteral(self):
        self.compareResourceOMO("native/returnCharacterLiteral.poc")

    def testReturnCharacterObject(self):
        self.compareResourceOMO("native/returnCharacterObject.poc")

    def testReturnCharacterValue(self):
        self.compareResourceOMO("native/returnCharacterValue.poc")

    def testReturnDecimalLiteral(self):
        self.compareResourceOMO("native/returnDecimalLiteral.poc")

    def testReturnIntegerLiteral(self):
        self.compareResourceOMO("native/returnIntegerLiteral.poc")

    def testReturnIntegerObject(self):
        self.compareResourceOMO("native/returnIntegerObject.poc")

    def testReturnIntegerValue(self):
        self.compareResourceOMO("native/returnIntegerValue.poc")

    def testReturnLongLiteral(self):
        self.compareResourceOMO("native/returnLongLiteral.poc")

    def testReturnLongObject(self):
        self.compareResourceOMO("native/returnLongObject.poc")

    def testReturnLongValue(self):
        self.compareResourceOMO("native/returnLongValue.poc")

    def testReturnStringLiteral(self):
        self.compareResourceOMO("native/returnStringLiteral.poc")


