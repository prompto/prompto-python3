from presto.parser.e.BaseEParserTest import BaseEParserTest
from presto.error.SyntaxError import SyntaxError
from presto.declaration.IDeclaration import IDeclaration
from presto.declaration.AttributeDeclaration import AttributeDeclaration
from presto.declaration.CategoryDeclaration import CategoryDeclaration
from presto.runtime.Context import MethodDeclarationMap

class TestScope(BaseEParserTest):

    def testAttribute(self):
        self.assertIsNone(self.context.getRegisteredDeclaration(IDeclaration, "id"))
        stmts = self.parseString("define id as: Integer attribute")
        self.assertIsNotNone(stmts)
        stmts.register(self.context)
        actual = self.context.getRegisteredDeclaration(IDeclaration, "id")
        self.assertIsNotNone(actual)
        self.assertIsInstance(actual, AttributeDeclaration)
        try:
            stmts.register(self.context)
            self.fail("Should raise SyntaxError")
        except SyntaxError:
            pass

    def testCategory(self):
        self.assertIsNone(self.context.getRegisteredDeclaration(IDeclaration, "Person"))
        stmts = self.parseString("define Person as: category with attributes: id and name")
        self.assertIsNotNone(stmts)
        stmts.register(self.context)
        actual = self.context.getRegisteredDeclaration(IDeclaration, "Person")
        self.assertIsNotNone(actual)
        self.assertIsInstance(actual, CategoryDeclaration)
        try:
            stmts.register(self.context)
            self.fail("Should raise SyntaxError")
        except SyntaxError:
            pass

    def testMethod(self):
        self.assertIsNone(self.context.getRegisteredDeclaration(IDeclaration, "printName"))
        stmts = self.parseString("define name as: Text attribute\r\n"
                                 + "define printName as: method receiving: name doing:\r\n"
                                 + "\tprint with \"name\" + name as value")
        self.assertIsNotNone(stmts)
        stmts.register(self.context)
        actual = self.context.getRegisteredDeclaration(IDeclaration, "printName")
        self.assertIsNotNone(actual)
        self.assertIsInstance(actual, MethodDeclarationMap)
        stmts = self.parseString("define printName as: method receiving: Person p doing:"
                                  + "\r\n\tprint with \"person\" + p.name as value")
        self.assertIsNotNone(stmts)
        stmts.register(self.context)
