from prompto.error.SyntaxError import SyntaxError
from prompto.expression.InstanceExpression import InstanceExpression
from prompto.expression.MemberSelector import MemberSelector
from prompto.expression.UnresolvedIdentifier import UnresolvedIdentifier
from prompto.runtime.Context import Context, InstanceContext
from prompto.value.NullValue import NullValue
from prompto.value.TypeValue import TypeValue


class MethodSelector(MemberSelector):

    def __init__(self, name, parent=None):
        super(MethodSelector, self).__init__(name, parent)

    def __str__(self):
        if self.parent == None:
            return self.name
        else:
            return str(self.parent) + '.' + self.name

    def toDialect(self, writer):
        if self.parent is None:
            writer.append(self.name)
        else:
            super(MethodSelector, self).toDialect(writer)

    def getCandidates(self, context:Context, checkInstance:bool):
        if self.parent is None:
            return self.getGlobalCandidates(context)
        else:
            return self.getMemberCandidates(context, checkInstance)

    def getGlobalCandidates(self, context:Context):
        from prompto.runtime.Context import MethodDeclarationMap
        methods = []
        # if called from a member method, could be a member method called without this/self
        if isinstance(context.getParentContext(), InstanceContext):
            from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
            typ = context.getParentContext().instanceType
            cd = context.getRegisteredDeclaration(ConcreteCategoryDeclaration, typ.typeName)
            if cd is not None:
                members = cd.getMemberMethods(context, self.name)
                if members is not None:
                    methods.extend(members)
        globs = context.getRegisteredDeclaration(MethodDeclarationMap, self.name)
        if globs is not None:
            methods.extend(globs.values())
        return methods


    def getMemberCandidates(self, context:Context, checkInstance:bool):
        parentType = self.checkParentType(context, checkInstance)
        return parentType.getMemberMethods(context, self.name)



    def checkParentType(self, context:Context, checkInstance:bool):
        if checkInstance:
            return self.checkParentInstance(context)
        else:
            return self.checkParent(context)



    def checkParentInstance(self, context:Context):
        name = None
        if isinstance(self.parent, InstanceExpression):
            name = self.parent.name
        elif isinstance(self.parent, UnresolvedIdentifier):
            name = self.parent.name
        if name is not None:
            # don't get Singleton values
            if name[0:1].islower():
                value = context.getValue(name)
                if value is not None and value is not NullValue.instance:
                    return value.type
        # TODO check result instance
        return self.checkParent(context)



    def getCategoryCandidates(self, context:Context):
        from prompto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
        from prompto.type.CategoryType import CategoryType
        type_ = self.checkParent(context)
        if not isinstance(type_, CategoryType):
            raise SyntaxError(self.parent.toString() + " is not a category")
        cd = context.getRegisteredDeclaration(ConcreteCategoryDeclaration, type_.typeName)
        if cd is None:
            raise SyntaxError("Unknown category:" + type_.typeName)
        return cd.getMemberMethods(context, self.name)



    def newLocalContext(self, context:Context, declaration):
        if self.parent is not None:
            return self.newInstanceContext(context)
        elif declaration.memberOf is not None:
            return self.newLocalInstanceContext(context)
        else:
            return context.newLocalContext()

    def newLocalCheckContext(self, context:Context, declaration):
        if self.parent is not None:
            return self.newInstanceCheckContext(context)
        elif declaration.memberOf is not None:
            return self.newLocalInstanceContext(context)
        else:
            return context.newLocalContext()



    def newLocalInstanceContext(self, context:Context):
        parent = context.getParentContext()
        if not isinstance(parent, InstanceContext):
            raise SyntaxError("Not in instance context !")
        context = context.newLocalContext()
        context.setParentContext(parent) # make local context child of the existing instance context
        return context



    def newInstanceCheckContext(self, context:Context):
        from prompto.type.CategoryType import CategoryType
        typ = self.parent.check (context)
        if isinstance(typ, CategoryType):
            context = context.newInstanceContext (None, typ)
            return context.newChildContext ()
        else:
            return context.newChildContext()



    def newInstanceContext(self, context:Context):
        value = self.parent.interpret(context)
        if value is None or value is NullValue.instance:
            from prompto.error.NullReferenceError import NullReferenceError
            raise NullReferenceError()
        from prompto.type.CategoryType import CategoryType
        if isinstance(value, TypeValue) and isinstance(value.value, CategoryType):
            value = context.loadSingleton(value.value)
        from prompto.value.ConcreteInstance import ConcreteInstance
        if isinstance(value, ConcreteInstance):
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
