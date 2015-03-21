from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestNative(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategory(self):
        self.compareResourceOEO("native/category.o")

    def testMethod(self):
        self.compareResourceOEO("native/method.o")

    def testReturn(self):
        self.compareResourceOEO("native/return.o")

    def testReturnBooleanLiteral(self):
        self.compareResourceOEO("native/returnBooleanLiteral.o")

    def testReturnBooleanObject(self):
        self.compareResourceOEO("native/returnBooleanObject.o")

    def testReturnBooleanValue(self):
        self.compareResourceOEO("native/returnBooleanValue.o")

    def testReturnCharacterLiteral(self):
        self.compareResourceOEO("native/returnCharacterLiteral.o")

    def testReturnCharacterObject(self):
        self.compareResourceOEO("native/returnCharacterObject.o")

    def testReturnCharacterValue(self):
        self.compareResourceOEO("native/returnCharacterValue.o")

    def testReturnDecimalLiteral(self):
        self.compareResourceOEO("native/returnDecimalLiteral.o")

    def testReturnIntegerLiteral(self):
        self.compareResourceOEO("native/returnIntegerLiteral.o")

    def testReturnIntegerObject(self):
        self.compareResourceOEO("native/returnIntegerObject.o")

    def testReturnIntegerValue(self):
        self.compareResourceOEO("native/returnIntegerValue.o")

    def testReturnLongObject(self):
        self.compareResourceOEO("native/returnLongObject.o")

    def testReturnLongValue(self):
        self.compareResourceOEO("native/returnLongValue.o")

    def testReturnStringLiteral(self):
        self.compareResourceOEO("native/returnStringLiteral.o")


