from prompto.error.SyntaxError import SyntaxError
from prompto.expression.MemberSelector import MemberSelector
from prompto.expression.MethodSelector import MethodSelector
from prompto.expression.SelectorExpression import SelectorExpression
from prompto.expression.UnresolvedIdentifier import UnresolvedIdentifier
from prompto.statement.UnresolvedCall import UnresolvedCall
from prompto.type.AnyType import AnyType



class UnresolvedSelector(SelectorExpression):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.resolved = None



    def __str__(self):
        return self.name if self.parent is None else str(self.parent) + '.' + self.name


    def toDialect(self, writer):
        try:
            self.resolve(writer.context, False)
        except:
            pass
        if self.resolved is not None:
            self.resolved.toDialect(writer)
        else:
            if self.parent is not None:
                self.parent.toDialect(writer)
                writer.append('.')
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
        return AnyType.instance if self.resolved is None else self.resolved.check(context)


    def resolve(self, context, forMember):
        if self.resolved is None:
            self.resolved = self.tryResolveMethod(context, None)
            if self.resolved is None:
                self.resolved = self.tryResolveMember(context)
        if self.resolved is None:
            raise SyntaxError("Unknown identifier:" + self.name)
        return self.resolved


    def resolveMethod(self, context, assignments):
        if self.resolved is None:
            self.resolved = self.tryResolveMethod(context, assignments)


    def tryResolveMember(self, context):
        try:
            member = MemberSelector(self.name, self.parent)
            member.check(context)
            return member
        except SyntaxError:
            return None


    def tryResolveMethod(self, context, assignments):
        try:
            resolvedParent = self.parent
            if isinstance(resolvedParent, UnresolvedIdentifier):
                resolvedParent.checkMember(context)
                resolvedParent = resolvedParent.resolved
            method = UnresolvedCall(MethodSelector(self.name, resolvedParent), assignments)
            method.check(context)
            return method
        except SyntaxError:
            return None

