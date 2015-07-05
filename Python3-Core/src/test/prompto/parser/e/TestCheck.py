from prompto.parser.e.BaseEParserTest import BaseEParserTest
from prompto.error.SyntaxError import SyntaxError

class TestCheck(BaseEParserTest):
    def testNativeAttribute(self):
        stmts = self.parseString("define id as: Integer attribute")
        stmts.register(self.context)
        stmts.check(self.context)

    def testUndeclaredCategoryAttribute(self):
        stmts = self.parseString("define person as: Person attribute")
        stmts.register(self.context)
        try:
            stmts.check(self.context)
            self.fail("Should fail since Person is not declared !")
        except SyntaxError:
            pass

    def testMethodAttribute(self):
        stmts = self.parseString("define name as: Text attribute\r\n" +
                                 "define printName as: method receiving: name doing:\r\n" +
                                 "\tprint with \"name\" + name as value\r\n" +
                                 "define Person as: category with attribute: printName")
        stmts.register(self.context)
        try:
            stmts.check(self.context)
            self.fail("Should fail since printName is not a category !")
        except SyntaxError:
            pass

    def testCategoryAttribute(self):
        stmts = self.parseString("define id as: Integer attribute\r\n" +
                                 "define Person as: category with attribute: id\r\n" +
                                 "define person as: Person attribute")
        stmts.register(self.context)
        stmts.check(self.context)

    def testCategoryWithUndeclaredDerived(self):
        stmts = self.parseString("define Employee as: Person")
        try:
            stmts.register(self.context)
            stmts.check(self.context)
            self.fail("Should fail since Person not declared !")
        except SyntaxError:
            pass


    def testCategoryWithUndeclaredAttribute(self):
        stmts = self.parseString("define Person as: category with attribute: id")
        try:
            stmts.register(self.context)
            stmts.check(self.context)
            self.fail("Should fail since id not declared !")
        except SyntaxError:
            pass


    def testCategory(self):
        stmts = self.parseString("define id as: Integer attribute\r\n" +
                                 "define Person as: category with attribute: id\r\n" +
                                 "define Employee as: Person")
        stmts.register(self.context)
        stmts.check(self.context)

    def testMethodWithUndeclaredAttribute(self):
        stmts = self.parseString("define printName as: method receiving: name doing:\r\n" +
                                 "\tprint with \"name\" + name as value")
        try:
            stmts.register(self.context)
            stmts.check(self.context)
            self.fail("Should fail since name not declared !")
        except SyntaxError:
            pass

    def testMethod(self):
        stmts = self.parseString("define print as: native method receiving: Text value doing:\r\n" +
                                 "\tJava: System.out.println(value);\r\n" +
                                 "define name as: Text attribute\r\n" +
                                 "define printName as: method receiving: name doing:\r\n" +
                                 "\tprint with \"name\" + name as value")
        stmts.register(self.context)
        stmts.check(self.context)

    def testList(self):
        stmts = self.parseString("define testMethod as: method receiving: Text value doing:\r\n" +
                                 "\tlist = [ \"john\" , \"jim\" ]\r\n" +
                                 "\telem = list[1]\r\n")
        stmts.register(self.context)
        stmts.check(self.context)

    def testDict(self):
        stmts = self.parseString("define testMethod as: method receiving: Text value doing:\r\n" +
                                 "\tdict = { \"john\":123, \"jim\":345 }\r\n" +
                                 "\telem = dict[\"john\"]\r\n")
        stmts.register(self.context)
        stmts.check(self.context)
