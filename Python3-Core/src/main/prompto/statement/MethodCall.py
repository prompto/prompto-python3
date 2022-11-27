from prompto.declaration.IDeclaration import IDeclaration
from prompto.declaration.AbstractMethodDeclaration import AbstractMethodDeclaration
from prompto.declaration.ArrowDeclaration import ArrowDeclaration
from prompto.error.PromptoError import PromptoError
from prompto.error.SyntaxError import SyntaxError
from prompto.grammar.ArgumentList import ArgumentList
from prompto.statement.SimpleStatement import SimpleStatement
from prompto.declaration.ConcreteMethodDeclaration import ConcreteMethodDeclaration
from prompto.runtime.Context import MethodDeclarationMap
from prompto.runtime.MethodFinder import MethodFinder
from prompto.declaration.ClosureDeclaration import ClosureDeclaration
from prompto.type.MethodType import MethodType
from prompto.type.VoidType import VoidType
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
        suffix = str(self.arguments) if self.arguments is not None else ""
        return str(self.selector) + suffix

    def check(self, context):
        finder = MethodFinder(context, self)
        declaration = finder.findBest(False)
        if declaration is None:
            return VoidType.instance
        if declaration.isAbstract():
            self.checkAbstractOnly(context, declaration)
            return VoidType.instance if declaration.returnType is None else declaration.returnType
        else:
            local = context if self.isLocalClosure(context) else self.selector.newLocalCheckContext(context, declaration)
            return self.checkDeclaration(declaration, context, local)

    def checkAbstractOnly(self, context, declaration):
        if declaration.isReference: # parameter or variable populated from a method call
            return
        if declaration.memberOf is not None: # the category could be subclassed (if constructor called on abstract, that would raise an error anyway)
                return
        # if a global method, need to check for runtime dispatch
        finder = MethodFinder(context, self)
        potential = finder.findPotential()
        if potential.all(lambda decl: decl.isAbstract()):
            raise SyntaxError("Cannot call abstract method")

    def checkReference(self, context):
        finder = MethodFinder(context, self)
        method = finder.findBest(False)
        if method is not None:
            return MethodType(method)
        else:
            return None

    def isLocalClosure(self, context):
        if self.selector.parent is not None:
            return False
        decl = context.getLocalDeclaration(IDeclaration, self.selector.name)
        return isinstance(decl, MethodDeclarationMap)

    def checkDeclaration(self, declaration, parent, local):
        if isinstance(declaration, ConcreteMethodDeclaration) and declaration.mustBeBeCheckedInCallContext(parent):
            return self.fullCheck(declaration, parent, local)
        else:
            return self.lightCheck(declaration, local)

    def lightCheck(self, declaration, local):
        declaration.registerParameters(local)
        return declaration.check(local)

    def fullCheck(self, declaration, parent, local):
        try:
            arguments = self.makeArguments(parent, declaration)
            declaration.registerParameters(local)
            for argument in arguments:
                expression = argument.resolve(local, declaration, True)
                value = argument.getParameter().checkValue(parent, expression)
                local.setValue(argument.getName(), value)
            return declaration.check(local)
        except PromptoError as e:
            raise SyntaxError(e.message)

    def makeArguments(self, context, declaration):
        if self.arguments is None:
            return ArgumentList()
        else:
            return self.arguments.makeArguments(context, declaration)

    def interpret(self, context):
        finder = MethodFinder(context, self)
        declaration = finder.findBest(True)
        if declaration is None:
            raise SyntaxError("No such method: " + str(self))
        local = self.selector.newLocalContext(context, declaration)
        declaration.registerParameters(local)
        self.assignArguments(context, local, declaration)
        return declaration.interpret(local)

    def assignArguments(self, context, local, declaration):
        arguments = self.makeArguments(context, declaration)
        for argument in arguments:
            expression = argument.resolve(local, declaration, True)
            parameter = argument.getParameter()
            value = parameter.checkValue(context, expression)
            if value is not None and parameter.mutable and not value.mutable:
                from prompto.error.NotMutableError import NotMutableError
                raise NotMutableError()
            local.setValue(argument.getName(), value)

    def interpretReference(self, context):
        declaration = self.findDeclaration(context)
        return ClosureValue(context, MethodType(declaration))


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
            return finder.findBest(True)


    def findRegistered(self, context):
        if self.selector.getParent() is None:
            try:
                o = context.getValue(self.selector.getName())
                if isinstance(o, ClosureValue):
                    return self.getClosureDeclaration(context, o)
                elif isinstance(o, ArrowValue):
                    return ArrowDeclaration(o)
            except PromptoError:
                pass
        return None


    def getClosureDeclaration(self, context, closure):
        decl = closure.itype.method
        if decl.memberOf is not None:
            # the closure references a member method (useful when a method reference is needed)
            # in which case we may simply want to return that method to avoid spilling context into method body
            # this is only true if the closure comes straight from the method's instance context
            # if the closure comes from an accessible context that is not the instance context
            # then it is a local variable that needs the closure context to be interpreted
            declaring = context.contextForValue(self.selector.getName())
            if declaring == closure.context:
                return decl
        return ClosureDeclaration(closure)


    def toDialect(self, writer):
        if self.requiresInvoke(writer):
            writer.append("invoke: ")
        self.selector.toDialect(writer, False)
        if self.arguments is not None:
            self.arguments.toDialect(writer)
        elif writer.dialect is not Dialect.E:
            writer.append("()")


    def requiresInvoke(self, writer):
        if writer.dialect is not Dialect.E or (self.arguments is not None and len(self.arguments) > 0):
            return False
        try:
            finder = MethodFinder(writer.context, self)
            declaration = finder.findBest(False)
            # if method is a reference, need to prefix with invoke
            return declaration.isAbstract() or declaration.closureOf is not None
        except:
            pass
            # ok
        return False