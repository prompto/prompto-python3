from presto.expression.MemberSelector import MemberSelector
from presto.error.SyntaxError import SyntaxError
from presto.value.NullValue import NullValue
from presto.value.TypeValue import TypeValue


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

    def getCandidates(self, context):
        if self.parent == None:
            return self.getGlobalCandidates(context)
        else:
            return self.getCategoryCandidates(context)

    def getGlobalCandidates(self, context):
        from presto.runtime.Context import MethodDeclarationMap
        actual = context.getRegisteredDeclaration(MethodDeclarationMap, self.name)
        if actual == None:
            raise SyntaxError("Unknown method: \"" + self.name + "\"")
        return actual.values()

    def getCategoryCandidates(self, context):
        from presto.declaration.ConcreteCategoryDeclaration import ConcreteCategoryDeclaration
        from presto.type.CategoryType import CategoryType
        type_ = self.checkParent(context)
        if not isinstance(type_, CategoryType):
            raise SyntaxError(self.parent.toString() + " is not a category")
        cd = context.getRegisteredDeclaration(ConcreteCategoryDeclaration, type_.getName())
        if cd is None:
            raise SyntaxError("Unknown category:" + type_.getName())
        return cd.findMemberMethods(context, self.name)

    def newLocalContext(self, context):
        if self.parent is None:
            return context.newLocalContext()
        else:
            return self.newInstanceContext(context)

    def newLocalCheckContext(self, context):
        if self.parent is None:
            return context.newLocalContext()
        else:
            return self.newInstanceCheckContext(context)

    def newInstanceCheckContext(self, context):
        from presto.type.CategoryType import CategoryType
        typ = self.parent.check (context)
        if not isinstance(typ, CategoryType):
            raise SyntaxError ("Not an instance !")
        context = context.newInstanceContext (None, typ)
        return context.newChildContext ()

    def newInstanceContext(self, context):
        value = self.parent.interpret(context)
        if value == None or value is NullValue.instance:
            from presto.error.NullReferenceError import NullReferenceError
            raise NullReferenceError()
        from presto.type.CategoryType import CategoryType
        if isinstance(value, TypeValue) and isinstance(value.value, CategoryType):
            value = context.loadSingleton(value.value)
        from presto.value.ConcreteInstance import ConcreteInstance
        if not isinstance(value, ConcreteInstance):
            from presto.error.InvalidDataError import InvalidDataError
            raise InvalidDataError("Not a concrete instance !")
        context = context.newInstanceContext(value, None)
        return context.newChildContext()

    def toInstanceExpression(self):
        if self.parent == None:
            from presto.grammar.UnresolvedIdentifier import UnresolvedIdentifier
            return UnresolvedIdentifier(self.name)
        else:
            return MemberSelector(self.parent, self.name)
