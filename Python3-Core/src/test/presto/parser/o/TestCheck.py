from presto.parser.o.BaseOParserTest import BaseOParserTest
from presto.runtime.utils.Out import Out
from presto.error.SyntaxError import SyntaxError


class TestCheck(BaseOParserTest):

    def setUp(self):
        super(type(self), self).setUp()

    def testNativeAttribute(self):
        stmts = self.parseString("attribute id: Integer;")
        stmts.register(self.context)
        stmts.check(self.context)

    def testUndeclaredCategoryAttribute(self):
        stmts = self.parseString("attribute person : Person;")
        stmts.register(self.context)
        try:
            stmts.check(self.context)
            self.fail("Should fail since Person is not declared !")
        except SyntaxError:
            pass

        def testMethodAttribute(self):
            stmts = self.parseString("attribute name: Text;" +
                                     "method PrintName(name) { " +
                                     "print ( value = \"name\" + name ); }" +
                                     "category Person extends PrintName;")
            stmts.register(self.context)
            try:
                stmts.check(self.context)
                self.fail("Should fail since printName is not a category !")
            except SyntaxError:
                pass

        def testCategoryAttribute(self):
            stmts = self.parseString("attribute id: Integer;" +
                                     "category Person(id);" +
                                     "attribute person: Person;")
            stmts.register(self.context)
            stmts.check(self.context)

        def testCategoryWithUndeclaredDerived(self):
            stmts = self.parseString("category Employee extends Person;")
            try:
                stmts.register(self.context)
                stmts.check(self.context)
                self.fail("Should fail since Person not declared !")
            except SyntaxError:
                pass

    def testCategoryWithUndeclaredAttribute(self):
        stmts = self.parseString("category Person(id);")
        try:
            stmts.register(self.context)
            stmts.check(self.context)
            self.fail("Should fail since id not declared !")
        except SyntaxError:
            pass

    def testCategory(self):
        stmts = self.parseString("attribute id: Integer;" +
                                 "category Person(id);" +
                                 "category Employee extends Person;")
        stmts.register(self.context)
        stmts.check(self.context)


    def testMethodWithUndeclaredAttribute(self):
        stmts = self.parseString("method printName(name) {" +
                                 "print (value = \"name\" + name ); }")
        try:
            stmts.register(self.context)
            stmts.check(self.context)
            self.fail("Should fail since name not declared !")
        except SyntaxError:
            pass


    def testMethod(self):
        stmts = self.parseString("native method print( Text value) {" +
                                 "Java: System.out.println(value); }" +
                                 "attribute name: Text;" +
                                 "method printName(name ) {" +
                                 "print( value = \"name\" + name ); }")
        stmts.register(self.context)
        stmts.check(self.context)


    def testList(self):
        stmts = self.parseString("method test (Text value) {" +
                                 "list = [ \"john\" , \"jim\" ];" +
                                 "elem = list[1]; }")
        stmts.register(self.context)
        stmts.check(self.context)


    def testDict(self):
        stmts = self.parseString("method test (Text value) {" +
                                 "dict = { \"john\":123, \"jim\":345 };" +
                                 "elem = dict[\"john\"]; }")
        stmts.register(self.context)
        stmts.check(self.context)
