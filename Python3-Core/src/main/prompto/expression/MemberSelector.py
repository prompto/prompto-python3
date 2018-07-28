from prompto.error.NullReferenceError import NullReferenceError
from prompto.expression.SelectorExpression import SelectorExpression
from prompto.expression.TypeExpression import TypeExpression
from prompto.expression.UnresolvedIdentifier import UnresolvedIdentifier
from prompto.parser.Dialect import Dialect
from prompto.type.MethodType import MethodType
from prompto.value.NullValue import NullValue


class MemberSelector (SelectorExpression):

    def __init__(self, name, parent = None):
        super().__init__(parent)
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return str(self.parent) + "." + self.name

    def toDialect(self, writer):
        if writer.dialect == Dialect.E:
            type = self.check(writer.context)
            if isinstance(type, MethodType):
                writer.append("Method: ")
        self.parentAndMemberToDialect(writer)


    def parentAndMemberToDialect(self, writer):
        try:
            self.resolveParent(writer.context)
        except:
            pass # ignore
        self.parent.toDialect(writer)
        writer.append(".")
        writer.append(self.name)

    def check(self, context):
        parentType = self.checkParent(context)
        return parentType.checkMember(context, self.name)

    def interpret(self, context):
        # resolve parent to keep clarity
        parent = self.resolveParent(context)
        # special case for singletons
        value = self.interpretSingleton(context, parent)
        if value is not None:
            return value
        # special case for 'static' type members (like Enum.symbols, Type.name etc...)
        value = self.interpretTypeMember(context, parent)
        if value is not None:
            return value
        # finally resolve instance member
        return self.interpretInstanceMember(context, parent)


    def interpretInstanceMember(self, context, parent):
        instance = parent.interpret(context)
        if instance is None or instance is NullValue.instance:
            raise NullReferenceError()
        else:
            return instance.getMemberValue(context, self.name, True)

    def interpretTypeMember(self, context, parent):
       if isinstance(parent, TypeExpression):
           return parent.getMemberValue(context, self.name)
       else:
           return None

    def interpretSingleton(self, context, parent):
        from prompto.type.EnumeratedCategoryType import EnumeratedCategoryType
        from prompto.type.CategoryType import CategoryType
        if isinstance(parent, TypeExpression) and isinstance(parent.type, CategoryType) and not isinstance(parent.type, EnumeratedCategoryType):
            instance = context.loadSingleton(parent.type)
            if instance is not None:
                return instance.getMemberValue(context, self.name, False)
        return None

    def resolveParent(self, context):
        if isinstance(self.parent, UnresolvedIdentifier):
            self.parent.checkMember(context)
            return self.parent.resolved
        else:
            return self.parent
