from prompto.declaration.AbstractMethodDeclaration import AbstractMethodDeclaration
from prompto.declaration.IDeclaration import IDeclaration
from prompto.runtime.Context import MethodDeclarationMap
from prompto.statement.SimpleStatement import SimpleStatement
from prompto.declaration.ConcreteMethodDeclaration import *
from prompto.grammar.ArgumentList import *
from prompto.runtime.MethodFinder import *
from prompto.declaration.ClosureDeclaration import ClosureDeclaration
from prompto.value.ClosureValue import ClosureValue
from prompto.value.Boolean import Boolean
from prompto.parser.Dialect import Dialect
from prompto.utils.CodeWriter import CodeWriter

class MethodCall(SimpleStatement):

    def __init__(self, selector, assignments=None):
        super().__init__()
        self.selector = selector
        self.assignments = assignments


    def __str__(self):
        suffix = str(self.assignments) if self.assignments != None else ""
        return str(self.selector) + suffix


    def check(self, context):
        finder = MethodFinder(context, self)
        declaration = finder.findMethod(False)
        local = context if self.isLocalClosure(context) else self.selector.newLocalCheckContext(context, declaration)
        return self.doCheck(declaration, context, local)


    def isLocalClosure(self, context):
        if self.selector.parent is not None:
            return False
        decl = context.getLocalDeclaration(IDeclaration, self.selector.name)
        return isinstance(decl, MethodDeclarationMap)


    def doCheck(self, declaration, parent, local):
        if isinstance(declaration, ConcreteMethodDeclaration) and declaration.mustBeBeCheckedInCallContext(parent):
            return self.fullCheck(declaration, parent, local)
        else:
            return self.lightCheck(declaration, local)


    def lightCheck(self, declaration, local):
        declaration.registerArguments(local)
        return declaration.check(local, False)


    def fullCheck(self, declaration, parent, local):
        try:
            assignments = self.makeAssignments(parent, declaration)
            declaration.registerArguments(local)
            for assignment in assignments:
                expression = assignment.resolve(local, declaration, True)
                value = assignment.getParameter().checkValue(parent, expression)
                local.setValue(assignment.getName(), value)
            return declaration.check(local, False)
        except PromptoError as e:
            raise SyntaxError(e.message)


    def makeAssignments(self, context, declaration):
        if self.assignments == None:
            return ArgumentList()
        else:
            return self.assignments.makeAssignments(context, declaration)


    def interpret(self, context):
        declaration = self.findDeclaration(context)
        local = self.selector.newLocalContext(context, declaration)
        declaration.registerArguments(local)
        assignments = self.makeAssignments(context, declaration)
        for assignment in assignments:
            expression = assignment.resolve(local, declaration, True)
            argument = assignment.getParameter()
            value = argument.checkValue(context, expression)
            if value is not None and argument.mutable and not value.mutable:
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
            o = context.getValue(self.selector.getName())
            if isinstance(o, ClosureValue):
                return ClosureDeclaration(o)
        except PromptoError:
            pass
        finder = MethodFinder(context, self)
        return finder.findMethod(True)


    def toDialect(self, writer):
        if self.requiresInvoke(writer):
            writer.append("invoke: ")
        self.selector.toDialect(writer)
        if self.assignments is not None:
            self.assignments.toDialect(writer)
        elif writer.dialect is not Dialect.E:
            writer.append("()")


    def requiresInvoke(self, writer):
        if writer.dialect is not Dialect.E or (self.assignments is not None and len(self.assignments) > 0):
            return False
        try:
            finder = MethodFinder(writer.context, self)
            declaration = finder.findMethod(False)
            # if method is abstract, need to prefix with invoke
            return isinstance(declaration, AbstractMethodDeclaration) or declaration.closureOf is not None
        except:
            return False
