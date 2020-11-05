from prompto.declaration.CategoryDeclaration import CategoryDeclaration
from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
from prompto.declaration.IDeclaration import IDeclaration
from prompto.error.SyntaxError import SyntaxError
from prompto.expression.ConstructorExpression import ConstructorExpression
from prompto.expression.IExpression import IExpression
from prompto.expression.MethodSelector import MethodSelector
from prompto.expression.SelectorExpression import SelectorExpression
from prompto.expression.UnresolvedIdentifier import UnresolvedIdentifier
from prompto.grammar.ArgumentList import ArgumentList
from prompto.grammar.INamed import INamed
from prompto.parser.Dialect import Dialect
from prompto.runtime.Context import Context, InstanceContext
from prompto.statement.BaseStatement import BaseStatement
from prompto.statement.MethodCall import MethodCall
from prompto.type.CategoryType import CategoryType
from prompto.type.MethodType import MethodType
from prompto.utils.CodeWriter import CodeWriter


class UnresolvedCall(BaseStatement):

    def __init__(self, caller:IExpression, arguments:ArgumentList):
        super().__init__()
        self.resolved = None
        self.caller = caller
        self.arguments = arguments


    def isSimple(self):
        return True


    def toDialect(self, writer):
        try:
            self.resolve(writer.context)
            self.resolved.toDialect(writer)
        except:
            self.caller.toDialect(writer)
            if self.arguments is not None:
                self.arguments.toDialect(writer)
            elif writer.dialect is not Dialect.E:
                writer.append("()")


    def check(self, context:Context):
        return self.resolveAndCheck(context)


    def interpret(self, context:Context):
        self.resolve(context)
        return self.resolved.interpret(context)


    def resolveAndCheck(self, context:Context):
        self.resolve(context)
        return self.resolved.check(context)


    def resolve(self, context:Context):
        from prompto.expression.UnresolvedSelector import UnresolvedSelector
        if self.resolved is None:
            if isinstance(self.caller, UnresolvedIdentifier):
                self.resolved = self.resolveUnresolvedIdentifier(context)
            elif isinstance(self.caller, UnresolvedSelector):
                self.resolved = self.resolveUnresolvedSelector(context)
            else:
                self.resolved = self.resolveMember(context)
        if self.resolved is None:
            raise SyntaxError("Unknown method: " + str(self))
        else:
            return self.resolved


    def resolveUnresolvedSelector(self, context:Context):
        self.caller.resolveMethod(context, self.arguments)
        return self.caller.resolved


    def resolveUnresolvedIdentifier(self, context:Context):
        name = self.caller.name
        # if this happens in the context of a member method, then we need to check for category members first
        call = self.resolveUnresolvedMemberMethod(context, name)
        if call is None:
            call = self.resolveUnresolvedMethodReference(context, name)
        if call is None:
            call = self.resolveUnresolvedDeclaration(context, name)
        if call is None:
            raise SyntaxError("Unknown name:" + name)
        else:
            return call


    def resolveUnresolvedMemberMethod(self, context, name):
        instance = context.getClosestInstanceContext()
        if instance is None:
            return None
        decl = self.resolveUnresolvedMember(instance, name)
        if decl is not None:
            return MethodCall(MethodSelector(name), self.arguments)
        else:
            return None


    def resolveUnresolvedMethodReference(self, context, name):
        # it could be a reference to a local closure
        named = context.getRegisteredValue(INamed, name)
        if named is None:
            return None
        itype = named.getType(context)
        if itype is not None:
            itype = itype.resolve(context)
            if isinstance(itype, MethodType):
                call = MethodCall(MethodSelector(name), self.arguments)
                call.variableName = name
                return call
        return None


    def resolveUnresolvedDeclaration(self, context, name):
        decl = context.getRegisteredDeclaration(IDeclaration, name)
        if decl is None:
            raise SyntaxError("Unknown name:" + name)
        if isinstance(decl, CategoryDeclaration):
            return ConstructorExpression(CategoryType(name), None, self.arguments)
        else:
            return MethodCall(MethodSelector(name), self.arguments)


    def resolveUnresolvedMember(self, context:InstanceContext, name:str):
        decl = context.getRegisteredDeclaration(ConcreteCategoryDeclaration, context.instanceType.typeName)
        methods = decl.getMemberMethodsMap(context, name)
        if methods is not None and len(methods)>0:
            return methods
        else:
            return None


    def resolveMember(self, context:Context):
        parent = self.caller.parent
        name = self.caller.name
        return MethodCall(MethodSelector(name, parent), self.arguments)


    def interpretAssert(self, context, testMethodDeclaration):
        self.resolve(context)
        if getattr(self.resolved, "interpretAssert", None) is not None:
            return self.resolved.interpretAssert(context, testMethodDeclaration)
        else:
            writer = CodeWriter(self.dialect, context)
            self.resolved.toDialect(writer)
            raise SyntaxError("Cannot test '" + str(writer) + "'")


    def setParent(self, parent):
        if parent is not None:
            if isinstance(self.caller, UnresolvedIdentifier):
                self.caller = MethodSelector(self.caller.name, parent)
            elif isinstance(self.caller, SelectorExpression):
                self.caller.parent = parent
            else:
                raise Exception("Should never happen!")
