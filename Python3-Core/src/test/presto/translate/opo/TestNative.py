from presto.parser.o.BaseOParserTest import BaseOParserTest

class TestNative(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategory(self):
        self.compareResourceOPO("native/category.o")

    def testMethod(self):
        self.compareResourceOPO("native/method.o")

    def testReturn(self):
        self.compareResourceOPO("native/return.o")

    def testReturnBooleanLiteral(self):
        self.compareResourceOPO("native/returnBooleanLiteral.o")

    def testReturnBooleanObject(self):
        self.compareResourceOPO("native/returnBooleanObject.o")

    def testReturnBooleanValue(self):
        self.compareResourceOPO("native/returnBooleanValue.o")

    def testReturnCharacterLiteral(self):
        self.compareResourceOPO("native/returnCharacterLiteral.o")

    def testReturnCharacterObject(self):
        self.compareResourceOPO("native/returnCharacterObject.o")

    def testReturnCharacterValue(self):
        self.compareResourceOPO("native/returnCharacterValue.o")

    def testReturnDecimalLiteral(self):
        self.compareResourceOPO("native/returnDecimalLiteral.o")

    def testReturnIntegerLiteral(self):
        self.compareResourceOPO("native/returnIntegerLiteral.o")

    def testReturnIntegerObject(self):
        self.compareResourceOPO("native/returnIntegerObject.o")

    def testReturnIntegerValue(self):
        self.compareResourceOPO("native/returnIntegerValue.o")

    def testReturnLongObject(self):
        self.compareResourceOPO("native/returnLongObject.o")

    def testReturnLongValue(self):
        self.compareResourceOPO("native/returnLongValue.o")

    def testReturnStringLiteral(self):
        self.compareResourceOPO("native/returnStringLiteral.o")


