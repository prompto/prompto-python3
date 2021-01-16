from prompto.expression.IExpression import IExpression
from prompto.expression.UnresolvedIdentifier import UnresolvedIdentifier
from prompto.expression.UnresolvedSelector import UnresolvedSelector
from prompto.parser.Dialect import Dialect
from prompto.runtime.Context import MethodDeclarationMap
from prompto.type.CategoryType import CategoryType
from prompto.type.MethodType import MethodType
from prompto.error.SyntaxError import SyntaxError
from prompto.value.ClosureValue import ClosureValue
from prompto.value.IInstance import IInstance
from prompto.value.NullValue import NullValue


class MethodExpression(IExpression):

    def __init__(self, expression):
        super(MethodExpression, self).__init__()
        self.expression = expression


    def getName(self):
        return self.expression


    def __str__(self):
        return "Method: " + str(self.expression)


    def check(self, context):
        expression = self.expression
        if isinstance(expression, UnresolvedSelector):
            parent = expression.parent
            if parent is not None:
                typ = parent.check(context)
                if isinstance(typ, CategoryType):
                    expression = UnresolvedIdentifier(expression.name, Dialect.O)
                    context = context.newInstanceContext(None, typ, True)
                else:
                    raise SyntaxError("Not a method: " + str(self.expression))
        if isinstance(expression, UnresolvedIdentifier):
            name = expression.name
            named = context.getRegistered(name)
            if isinstance(named, MethodDeclarationMap):
                method = named.getFirst()
                return MethodType(method)
            else:
                raise SyntaxError("No method with name:" + name)
        else:
            return SyntaxError("Not implemented !")

    def interpret(self, context):
        expression = self.expression
        if isinstance(expression, UnresolvedSelector):
            parent = expression.parent
            if parent is not None:
                value = parent.interpret(context)
                if isinstance(value, IInstance):
                    expression = UnresolvedIdentifier(expression.name, Dialect.O)
                    context = context.newInstanceContext(value, None, True)
                else:
                    return NullValue.instance
        if isinstance(expression, UnresolvedIdentifier):
            name = expression.name
            if context.hasValue(name):
                return context.getValue(name)
            else:
                named = context.getRegistered(name)
                if isinstance(named, MethodDeclarationMap):
                    decl = named.getFirst()
                    return ClosureValue(context, MethodType(decl))
                else:
                    raise SyntaxError("No method with name:" + name)


    def toDialect(self, writer):
        if writer.dialect is Dialect.E:
            writer.append("Method: ")
        writer.append(str(self.expression))
