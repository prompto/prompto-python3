from prompto.declaration.BaseDeclaration import BaseDeclaration
from prompto.type.VoidType import VoidType
from prompto.error.ExecutionError import ExecutionError

class TestMethodDeclaration(BaseDeclaration):
    
    def __init__(self, name, stmts, exps, error):
        super().__init__(name)
        self.statements = stmts
        self.assertions = exps
        self.error = error

    def check(self, context):
        # TODO
        return VoidType.instance
    
    def register(self, context):
        context.registerTestDeclaration (self)
    
    def getType(self, context):
        return VoidType.instance
    
    def interpret(self, context):
        if self.interpretBody (context):
            self.interpretNoError (context)
            self.interpretAsserts (context)
    
    def interpretNoError(self, context):
        # we land here only if no error was raised
        if self.error is not None:
            self.printMissingError (context, self.error.name, "no error")
    
    def interpretAsserts(self, context):
        if self.assertions is None:
            return
        context.enterMethod (self)
        try:
            success = True
            for a in self.assertions:
                success &= a.interpretAssert (context, self)
            if success:
                self.printSuccess (context)
        finally:
            context.leaveMethod (self)
    
    def printMissingError(self, context, expected, actual):
        print (self.name + " test failed while expecting: " + expected + ", found: " + actual, end='')

    def printFailedAssertion(self, context, expected, actual):
        print (self.name + " test failed while verifying: " + expected + ", found: " + actual, end='')
    
    def printSuccess(self, context):
        print (self.name + " test successful", end='')
    
    def interpretBody(self, context):
        context.enterMethod (self)
        try:
            self.statements.interpret (context)
            return True
        except ExecutionError as e:
            self.interpretError (context, e)
            # no more to execute
            return False
        finally:
            context.leaveMethod (self)
    
    def interpretError(self, context, ex):
        actual = ex.interpret (context, "__test_error__")
        expectedError = None if self.error is None else self.error.interpret (context)
        if expectedError == actual:
            self.printSuccess (context)
        else:
            actualName = str(actual.getMemberValue (context, "name"))
            expectedName = "SUCCESS" if self.error is None else self.error.name
            self.printMissingError (context, expectedName, actualName)
    
    def toDialect(self, writer):
        if writer.isGlobalContext ():
            writer = writer.newLocalWriter ()
        super().toDialect(writer)
    
    def toMDialect(self, writer):
        writer.append ("def test ")
        writer.append (self.name)
        writer.append (" ():\n")
        writer.indent ()
        self.statements.toDialect (writer)
        writer.dedent ()
        writer.append ("verifying:")
        if self.error is not None:
            writer.append (" ")
            self.error.toDialect (writer)
            writer.append ("\n")
        else:
            writer.append ("\n")
            writer.indent ()
            for a in self.assertions:
                a.toDialect (writer)
                writer.append ("\n")
            writer.dedent ()

    def toEDialect(self, writer):
        writer.append ("define ")
        writer.append (self.name)
        writer.append (" as test method doing:\n")
        writer.indent ()
        self.statements.toDialect (writer)
        writer.dedent ()
        writer.append ("and verifying")
        if self.error is not None:
            writer.append (" ")
            self.error.toDialect (writer)
            writer.append ("\n")
        else:
            writer.append (":\n")
            writer.indent ()
            for a in self.assertions:
                a.toDialect (writer)
                writer.append ("\n")
            writer.dedent ()

    def toODialect(self, writer):
        writer.append ("test method ")
        writer.append (self.name)
        writer.append (" () {\n")
        writer.indent ()
        self.statements.toDialect (writer)
        writer.dedent ()
        writer.append ("} verifying ")
        if self.error is not None:
            self.error.toDialect (writer)
            writer.append (";\n")
        else:
            writer.append ("{\n")
            writer.indent ()
            for a in self.assertions:
                a.toDialect (writer)
                writer.append (";\n")
            writer.dedent ()
            writer.append ("}\n")

