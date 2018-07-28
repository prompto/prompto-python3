from prompto.expression.IExpression import IExpression
from prompto.parser.Dialect import Dialect
from prompto.runtime.Context import MethodDeclarationMap
from prompto.type.MethodType import MethodType
from prompto.error.SyntaxError import SyntaxError
from prompto.value.ClosureValue import ClosureValue



class MethodExpression(IExpression):

    def __init__(self, name):
        super(MethodExpression, self).__init__()
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return "Method: " + self.name

    def check(self, context):
        named = context.getRegistered(self.name)
        if isinstance(named, MethodDeclarationMap):
            method = named.getFirst()
            return MethodType(method)
        else:
            raise SyntaxError("No method with name:" + self.name)

    def interpret(self, context):
        if context.hasValue(self.name):
            return context.getValue(self.name)
        else:
            named = context.getRegistered(self.name)
            if isinstance(named, MethodDeclarationMap):
                decl = named.getFirst()
                return ClosureValue(context, MethodType(decl))
            else:
                raise SyntaxError("No method with name:" + self.name)


    def toDialect(self, writer):
        if writer.dialect is Dialect.E:
            writer.append("Method: ")
        writer.append(self.name)
