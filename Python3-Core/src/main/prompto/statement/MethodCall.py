from prompto.declaration.AbstractMethodDeclaration import AbstractMethodDeclaration
from prompto.declaration.ArrowDeclaration import ArrowDeclaration
from prompto.declaration.IDeclaration import IDeclaration
from prompto.runtime.Context import MethodDeclarationMap
from prompto.statement.SimpleStatement import SimpleStatement
from prompto.declaration.ConcreteMethodDeclaration import *
from prompto.grammar.ArgumentList import *
from prompto.runtime.MethodFinder import *
from prompto.declaration.ClosureDeclaration import ClosureDeclaration
from prompto.value.ArrowValue import ArrowValue
from prompto.value.ClosureValue import ClosureValue
from prompto.value.BooleanValue import BooleanValue
from prompto.parser.Dialect import Dialect
from prompto.utils.CodeWriter import CodeWriter

class MethodCall(SimpleStatement):

    def __init__(self, selector, arguments=None):
        super().__init__()
        self.selector = selector
        self.arguments = arguments


    def __str__(self):
        suffix = str(self.arguments) if self.arguments != None else ""
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
            arguments = self.makeArguments(parent, declaration)
            declaration.registerArguments(local)
            for argument in arguments:
                expression = argument.resolve(local, declaration, True)
                value = argument.getParameter().checkValue(parent, expression)
                local.setValue(argument.getName(), value)
            return declaration.check(local, False)
        except PromptoError as e:
            raise SyntaxError(e.message)


    def makeArguments(self, context, declaration):
        if self.arguments == None:
            return ArgumentList()
        else:
            return self.arguments.makeArguments(context, declaration)


    def interpret(self, context):
        declaration = self.findDeclaration(context)
        local = self.selector.newLocalContext(context, declaration)
        declaration.registerArguments(local)
        arguments = self.makeArguments(context, declaration)
        for argument in arguments:
            expression = argument.resolve(local, declaration, True)
            parameter = argument.getParameter()
            value = parameter.checkValue(context, expression)
            if value is not None and parameter.mutable and not value.mutable:
                from prompto.error.NotMutableError import NotMutableError
                raise NotMutableError()
            local.setValue(argument.getName(), value)
        return declaration.interpret(local)


    def interpretAssert(self, context, testMethodDeclaration):
        value = self.interpret(context)
        if isinstance(value, BooleanValue):
            return value.value
        else:
            writer = CodeWriter(self.dialect, context)
            self.toDialect(writer)
            raise SyntaxError("Cannot test '" + str(writer) + "'")


    def findDeclaration(self, context):
        method = self.findRegistered(context)
        if method is not None:
            return method
        else:
            finder = MethodFinder(context, self)
            return finder.findMethod(True)


    def findRegistered(self, context):
        if self.selector.getParent() is None:
            try:
                o = context.getValue(self.selector.getName())
                if isinstance(o, ClosureValue):
                    return ClosureDeclaration(o)
                elif isinstance(o, ArrowValue):
                    return ArrowDeclaration(o)
            except PromptoError:
                pass
        return None


    def toDialect(self, writer):
        if self.requiresInvoke(writer):
            writer.append("invoke: ")
        self.selector.toDialect(writer)
        if self.arguments is not None:
            self.arguments.toDialect(writer)
        elif writer.dialect is not Dialect.E:
            writer.append("()")


    def requiresInvoke(self, writer):
        if writer.dialect is not Dialect.E or (self.arguments is not None and len(self.arguments) > 0):
            return False
        try:
            finder = MethodFinder(writer.context, self)
            declaration = finder.findMethod(False)
            # if method is abstract, need to prefix with invoke
            return isinstance(declaration, AbstractMethodDeclaration) or declaration.closureOf is not None
        except:
            return False
