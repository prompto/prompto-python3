from prompto.parser.o.BaseOParserTest import BaseOParserTest

class TestNative(BaseOParserTest):
    
    def setUp(self):
        super(type(self), self).setUp()
    
    def testCategory(self):
        self.compareResourceOSO("native/category.poc")

    def testMethod(self):
        self.compareResourceOSO("native/method.poc")

    def testReturn(self):
        self.compareResourceOSO("native/return.poc")

    def testReturnBooleanLiteral(self):
        self.compareResourceOSO("native/returnBooleanLiteral.poc")

    def testReturnBooleanObject(self):
        self.compareResourceOSO("native/returnBooleanObject.poc")

    def testReturnBooleanValue(self):
        self.compareResourceOSO("native/returnBooleanValue.poc")

    def testReturnCharacterLiteral(self):
        self.compareResourceOSO("native/returnCharacterLiteral.poc")

    def testReturnCharacterObject(self):
        self.compareResourceOSO("native/returnCharacterObject.poc")

    def testReturnCharacterValue(self):
        self.compareResourceOSO("native/returnCharacterValue.poc")

    def testReturnDecimalLiteral(self):
        self.compareResourceOSO("native/returnDecimalLiteral.poc")

    def testReturnIntegerLiteral(self):
        self.compareResourceOSO("native/returnIntegerLiteral.poc")

    def testReturnIntegerObject(self):
        self.compareResourceOSO("native/returnIntegerObject.poc")

    def testReturnIntegerValue(self):
        self.compareResourceOSO("native/returnIntegerValue.poc")

    def testReturnLongLiteral(self):
        self.compareResourceOSO("native/returnLongLiteral.poc")

    def testReturnLongObject(self):
        self.compareResourceOSO("native/returnLongObject.poc")

    def testReturnLongValue(self):
        self.compareResourceOSO("native/returnLongValue.poc")

    def testReturnStringLiteral(self):
        self.compareResourceOSO("native/returnStringLiteral.poc")


