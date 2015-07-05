from prompto.declaration.AbstractMethodDeclaration import AbstractMethodDeclaration
from prompto.statement.SimpleStatement import SimpleStatement
from prompto.declaration.ConcreteMethodDeclaration import *
from prompto.grammar.ArgumentAssignmentList import *
from prompto.runtime.MethodFinder import *
from prompto.declaration.ClosureDeclaration import ClosureDeclaration
from prompto.value.ClosureValue import ClosureValue
from prompto.value.Boolean import Boolean
from prompto.parser.Dialect import Dialect
from prompto.utils.CodeWriter import CodeWriter

class MethodCall(SimpleStatement):

    def __init__(self, method, assignments=None):
        super().__init__()
        self.method = method
        self.assignments = assignments

    def getMethod(self):
        return self.method

    def getAssignments(self):
        return self.assignments

    def __str__(self):
        suffix = str(self.assignments) if self.assignments != None else ""
        return str(self.method) + suffix

    def check(self, context):
        finder = MethodFinder(context, self)
        declaration = finder.findMethod(False)
        local = self.method.newLocalCheckContext(context, declaration)
        return self.doCheck(declaration, context, local)


    def doCheck(self, declaration, parent, local):
        if isinstance(declaration, ConcreteMethodDeclaration) and declaration.mustBeBeCheckedInCallContext(parent):
            return self.fullCheck(declaration, parent, local)
        else:
            return self.lightCheck(declaration, parent, local)

    def lightCheck(self, declaration, parent, local):
        declaration.registerArguments(local)
        return declaration.check(local)

    def fullCheck(self, declaration, parent, local):
        try:
            assignments = self.makeAssignments(parent, declaration)
            declaration.registerArguments(local)
            for assignment in assignments:
                expression = assignment.resolve(local, declaration, True)
                value = assignment.getArgument().checkValue(parent, expression)
                local.setValue(assignment.getName(), value)
            return declaration.check(local)
        except PrestoError as e:
            raise SyntaxError(e.message)

    def makeAssignments(self, context, declaration):
        if self.assignments == None:
            return ArgumentAssignmentList()
        else:
            return self.assignments.makeAssignments(context, declaration)

    def interpret(self, context):
        declaration = self.findDeclaration(context)
        local = self.method.newLocalContext(context, declaration)
        declaration.registerArguments(local)
        assignments = self.makeAssignments(context, declaration)
        for assignment in assignments:
            expression = assignment.resolve(local, declaration, True)
            argument = assignment.getArgument()
            value = argument.checkValue(context, expression)
            if value is not None and value.mutable and not argument.mutable:
                from prompto.error.NotMutableError import NotMutableError
                raise NotMutableError()
            local.setValue(assignment.getName(), value)
        return declaration.interpret(local)

    def interpretAssert(self, context, testMethodDeclaration):
        value = self.interpret(context)
        if isinstance(value, Boolean):
            return value.value
        else:
            writer = CodeWriter(self.dialect, context)
            self.toDialect(writer)
            raise SyntaxError("Cannot test '" + str(writer) + "'")

    def findDeclaration(self, context):
        try:
            o = context.getValue(self.method.getName())
            if isinstance(o, ClosureValue):
                return ClosureDeclaration(o)
        except PrestoError:
            pass
        finder = MethodFinder(context, self)
        return finder.findMethod(True)

    def toDialect(self, writer):
        if self.requiresInvoke(writer):
            writer.append("invoke: ")
        self.method.toDialect(writer)
        if self.assignments is not None:
            self.assignments.toDialect(writer)
        elif writer.dialect is not Dialect.E:
            writer.append("()")

    def requiresInvoke(self, writer):
        if writer.dialect is not Dialect.E:
            return False
        if self.assignments is not None and len(self.assignments) > 0:
            return False
        try:
            finder = MethodFinder(writer.context, self)
            declaration = finder.findMethod(False)
            # if method is abstract, need to prefix with invoke
            if isinstance(declaration, AbstractMethodDeclaration):
                return True
        except:
            pass
            # ok
        return False
