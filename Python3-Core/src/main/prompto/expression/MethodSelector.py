from prompto.declaration.IMethodDeclaration import IMethodDeclaration
from prompto.error.NullReferenceError import NullReferenceError
from prompto.error.SyntaxError import SyntaxError
from prompto.expression.MemberSelector import MemberSelector
from prompto.grammar.INamedInstance import INamedInstance
from prompto.runtime.Context import Context, InstanceContext
from prompto.type.MethodType import MethodType
from prompto.value.NullValue import NullValue
from prompto.value.TypeValue import TypeValue


class MethodSelector(MemberSelector):

    def __init__(self, name, parent=None):
        super(MethodSelector, self).__init__(name, parent)


    def __str__(self):
        if self.parent is None:
            return self.name
        else:
            return str(self.parent) + '.' + self.name


    def toDialect(self, writer):
        if self.parent is None:
            writer.append(self.name)
        else:
            super(MethodSelector, self).parentAndMemberToDialect(writer)


    def getCandidates(self, context:Context, checkInstance:bool):
        method = self.getMethodInstance(context)
        if method is not None:
            return {method}
        elif self.parent is None:
            return self.getGlobalCandidates(context)
        else:
            return self.getMemberCandidates(context, checkInstance)


    def getMethodInstance(self, context):
        named = context.getRegistered(self.name)
        if isinstance(named, INamedInstance):
            typ = named.getType(context)
            if typ is not None:
                typ = typ.resolve(context)
                if isinstance(typ, MethodType):
                    return typ.method
        return None


    def getGlobalCandidates(self, context:Context):
        from prompto.runtime.Context import MethodDeclarationMap
        methods = set()
        # if called from a member method, could be a member method called without this/self
        parentContext = context.getParentContext()
        if isinstance(parentContext, InstanceContext):
            from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
            typ = parentContext.instanceType
            cd = context.getRegisteredDeclaration(ConcreteCategoryDeclaration, typ.typeName)
            if cd is not None:
                members = cd.getMemberMethodsMap(context, self.name)
                if members is not None:
                    methods.update(members.values())
        globals = context.getRegisteredDeclaration(MethodDeclarationMap, self.name)
        if globals is not None:
            methods.update(globals.values())
        return methods


    def getMemberCandidates(self, context:Context, checkInstance:bool):
        parentType = self.checkParentType(context, checkInstance)
        methods = parentType.getMemberMethods(context, self.name)
        return set(methods)


    def checkParentType(self, context:Context, checkInstance:bool):
        if checkInstance:
            return self.interpretParentInstance(context)
        else:
            return self.checkParent(context)


    def interpretParentInstance(self, context:Context):
        value = self.parent.interpret(context)
        if value is None or value == NullValue.instance:
            raise NullReferenceError()
        from prompto.expression.SuperExpression import SuperExpression
        if isinstance(self.parent, SuperExpression):
            return value.itype.getSuperType(context)
        else:
            return value.itype


    def getCategoryCandidates(self, context:Context):
        from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
        from prompto.type.CategoryType import CategoryType
        itype = self.checkParent(context)
        if not isinstance(itype, CategoryType):
            raise SyntaxError(self.parent.toString() + " is not a category")
        cd = context.getRegisteredDeclaration(ConcreteCategoryDeclaration, itype.typeName)
        if cd is None:
            raise SyntaxError("Unknown category:" + itype.typeName)
        return cd.getMemberMethods(context, self.name)


    def newLocalContext(self, context:Context, declaration):
        if self.parent is not None:
            return self.newInstanceContext(context)
        elif declaration.memberOf is not None:
            return self.newLocalInstanceContext(context, declaration)
        else:
            return context.newLocalContext()


    def newLocalCheckContext(self, context:Context, declaration):
        if self.parent is not None:
            return self.newInstanceCheckContext(context)
        elif declaration.memberOf is not None:
            return self.newLocalInstanceContext(context, declaration)
        else:
            return context.newLocalContext()


    def newLocalInstanceContext(self, context:Context, declaration:IMethodDeclaration):
        instance = context.getClosestInstanceContext()
        if instance is not None:
            required = declaration.memberOf.getType(context)
            actual = instance.instanceType
            if not required.isAssignableFrom(context, actual):
                instance = None
        if instance is None:
            declaring = declaration.memberOf.getType(context)
            instance = context.newInstanceContext(declaring, False)
        return instance.newChildContext()


    def newInstanceCheckContext(self, context:Context):
        from prompto.type.CategoryType import CategoryType
        from prompto.type.TypeType import TypeType
        from prompto.declaration.IDeclaration import IDeclaration
        from prompto.declaration.SingletonCategoryDeclaration import SingletonCategoryDeclaration
        typ = self.parent.check (context)
        # if calling singleton method, parent is the singleton type
        if isinstance(typ, TypeType):
            decl = context.getRegisteredDeclaration(IDeclaration, typ.typ.typeName)
            if isinstance(decl, SingletonCategoryDeclaration):
                typ = decl.getType(context)
        if isinstance(typ, CategoryType):
            context = context.newInstanceContext (None, typ)
            return context.newChildContext ()
        else:
            return context.newChildContext()


    def newInstanceContext(self, context:Context):
        from prompto.type.CategoryType import CategoryType
        from prompto.expression.CategorySymbol import CategorySymbol
        from prompto.value.ConcreteInstance import ConcreteInstance
        from prompto.value.NativeInstance import NativeInstance
        from prompto.declaration.SingletonCategoryDeclaration import SingletonCategoryDeclaration

        value = self.parent.interpret(context)
        if value is None or value is NullValue.instance:
            from prompto.error.NullReferenceError import NullReferenceError
            raise NullReferenceError()
        if isinstance(value, TypeValue):
            typ = value.value
            if isinstance(typ, CategoryType):
                decl = typ.getDeclaration(context)
                if isinstance(decl, SingletonCategoryDeclaration):
                    value = context.loadSingleton(value.value)
        if isinstance(value, CategorySymbol):
            value = value.interpret(context)
        if isinstance(value, TypeValue):
            return context.newChildContext()
        elif isinstance(value, (ConcreteInstance, NativeInstance)):
            context = context.newInstanceContext(value, None)
            return context.newChildContext()
        else:
            context = context.newBuiltInContext(value)
            return context.newChildContext()


    def toInstanceExpression(self):
        if self.parent is None:
            from prompto.expression.UnresolvedIdentifier import UnresolvedIdentifier
            return UnresolvedIdentifier(self.name)
        else:
            return MemberSelector(self.parent, self.name)
