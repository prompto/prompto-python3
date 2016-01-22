from prompto.declaration.EnumeratedNativeDeclaration import EnumeratedNativeDeclaration
from prompto.expression.ConstructorExpression import ConstructorExpression
from prompto.expression.IExpression import IExpression
from prompto.expression.InstanceExpression import *
from prompto.error.SyntaxError import SyntaxError
from prompto.expression.SymbolExpression import SymbolExpression
from prompto.expression.TypeExpression import TypeExpression
from prompto.type.NativeType import NativeType


class UnresolvedIdentifier(IExpression):
    def __init__(self, name):
        self.name = name
        self.resolved = None

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

    def toDialect(self, writer):
        try:
            self.resolve(writer.context, False)
            self.resolved.toDialect(writer)
        except:
            writer.append(self.name)

    def check(self, context):
        return self.resolveAndCheck(context, False)

    def checkMember(self, context):
        return self.resolveAndCheck(context, True)

    def interpret(self, context):
        self.resolveAndCheck(context, False)
        return self.resolved.interpret(context)

    def resolveAndCheck(self, context, forMember):
        self.resolve(context, forMember)
        return self.resolved.check(context)

    def resolve(self, context, forMember):
        if self.resolved is None:
            self.resolved = self.resolveSymbol(context)
            if self.resolved is None:
                if self.name[0].isupper():
                    if forMember:
                        self.resolved = self.resolveType(context)
                    else:
                        self.resolved = self.resolveConstructor(context)
                if self.resolved is None:
                    self.resolved = self.resolveMethod(context)
                    if self.resolved is None:
                        self.resolved = self.resolveInstance(context)
        if self.resolved is None:
            # no other alternative
            raise SyntaxError("Unknown identifier:" + self.name)
        else:
            return self.resolved


    def resolveSymbol(self, context):
        if self.name.isupper():
            return SymbolExpression(self.name)
        else:
            return None

    def resolveType(self, context):
        from prompto.declaration.CategoryDeclaration import CategoryDeclaration
        from prompto.type.CategoryType import CategoryType
        decl = context.getRegisteredDeclaration(IDeclaration, self.name)
        if isinstance(decl, CategoryDeclaration):
            return TypeExpression(CategoryType(self.name))
        elif isinstance(decl, EnumeratedNativeDeclaration):
            return TypeExpression(decl.getType(context))
        else:
            for type in NativeType.getAll():
                if self.name==type.getName():
                    return TypeExpression(type)
        return None

    def resolveConstructor(self, context):
        from prompto.type.CategoryType import CategoryType
        try:
            ctor = ConstructorExpression(CategoryType(self.name), False, None)
            ctor.check(context)
            return ctor
        except SyntaxError as e:
            return None

    def resolveMethod(self, context):
        from prompto.statement.MethodCall import MethodCall
        from prompto.expression.MethodSelector import MethodSelector
        try:
            method = MethodCall(MethodSelector(self.name))
            method.check(context)
            return method
        except SyntaxError:
            return None

    def resolveInstance(self, context):
        try:
            inst = InstanceExpression(self.name)
            inst.check(context)
            return inst
        except SyntaxError:
            return None