from prompto.declaration.EnumeratedNativeDeclaration import EnumeratedNativeDeclaration
from prompto.declaration.IDeclaration import IDeclaration
from prompto.expression.ConstructorExpression import ConstructorExpression
from prompto.expression.InstanceExpression import InstanceExpression
from prompto.expression.IExpression import IExpression
from prompto.error.SyntaxError import SyntaxError
from prompto.expression.SymbolExpression import SymbolExpression
from prompto.expression.TypeExpression import TypeExpression
from prompto.parser.Dialect import Dialect
from prompto.type.AnyType import AnyType
from prompto.type.NativeType import NativeType


class UnresolvedIdentifier(IExpression):

    def __init__(self, name, dialect):
        self.name = name
        self.dialect = dialect
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


    def checkReference(self, context):
        self.resolve(context, False)
        return self.resolved.checkReference(context) if self.resolved else AnyType.instance


    def checkAttribute(self, context):
        self.resolve(context, False)
        return self.resolved.checkAttribute(context)


    def checkQuery(self, context):
        return self.check(context)


    def checkMember(self, context):
        return self.resolveAndCheck(context, True)


    def interpret(self, context):
        self.resolveAndCheck(context, False)
        return self.resolved.interpret(context)


    def interpretReference(self, context):
        self.resolveAndCheck(context, False)
        return self.resolved.interpretReference(context)


    def interpretQuery(self, context, builder):
        self.resolveAndCheck(context, False)
        self.resolved.interpretQuery(context, builder)


    def resolveAndCheck(self, context, forMember):
        self.resolve(context, forMember)
        return self.resolved.check(context)


    def resolve(self, context, forMember):
        if self.resolved is None:
            self.resolved = self.doResolve(context, forMember)
        if self.resolved is None:
            # no other alternative
            raise SyntaxError("Unknown identifier:" + self.name)
        else:
            return self.resolved


    def doResolve(self, context, forMember):
        resolved = self.resolveSymbol(context)
        if resolved is not None:
            return resolved
        resolved = self.resolveTypeOrConstructor(context, forMember)
        if resolved is not None:
            return resolved
        resolved = self.resolveMethodCall(context)
        if resolved is not None:
            return resolved
        resolved = self.resolveInstance(context)
        return resolved


    def resolveTypeOrConstructor(self, context, forMember):
        if not self.name[0].isupper():
            return None
        if forMember:
            return self.resolveType(context)
        else:
            return self.resolveConstructor(context)


    def resolveSymbol(self, context):
        if self.name.isupper():
            return SymbolExpression(self.name)
        else:
            return None

    def resolveType(self, context):
        from prompto.declaration.EnumeratedCategoryDeclaration import EnumeratedCategoryDeclaration
        from prompto.declaration.CategoryDeclaration import CategoryDeclaration
        from prompto.type.EnumeratedCategoryType import EnumeratedCategoryType
        from prompto.type.CategoryType import CategoryType
        decl = context.getRegisteredDeclaration(IDeclaration, self.name)
        if isinstance(decl, EnumeratedCategoryDeclaration):
            return TypeExpression(EnumeratedCategoryType(self.name))
        elif isinstance(decl, CategoryDeclaration):
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
            ctor = ConstructorExpression(CategoryType(self.name), None, None, True)
            ctor.check(context)
            return ctor
        except SyntaxError as e:
            return None


    def resolveMethodCall(self, context):
        if not self.dialect is Dialect.E:
            return None
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
