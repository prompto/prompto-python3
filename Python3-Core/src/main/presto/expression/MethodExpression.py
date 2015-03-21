from presto.expression.IExpression import IExpression
from presto.parser.Dialect import Dialect
from presto.runtime.Context import MethodDeclarationMap
from presto.type.MethodType import MethodType
from presto.error.SyntaxError import SyntaxError


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
            return MethodType(context, self.name)
        else:
            raise SyntaxError("No method with name:" + self.name)

    def interpret(self, context):
        return context.getValue(self.name)

    def toDialect(self, writer):
        if writer.dialect is Dialect.E:
            writer.append("Method: ")
        writer.append(self.name)
