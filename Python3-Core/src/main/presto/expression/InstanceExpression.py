from presto.grammar.IArgument import *
from presto.parser.Dialect import Dialect
from presto.runtime.Context import *
from presto.runtime.LinkedVariable import LinkedVariable
from presto.runtime.Variable import *
from presto.type.MethodType import *


class InstanceExpression(IExpression):

    def __init__(self, name):
        super(InstanceExpression, self).__init__()
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

    def toDialect(self, writer, requireMethod = True):
        if requireMethod and self.requiresMethod(writer):
            writer.append("Method: ")
        writer.append(self.name)

    def requiresMethod(self, writer):
        if writer.dialect is not Dialect.E:
            return False
        o = writer.context.getRegistered(self.name)
        if isinstance(o, MethodDeclarationMap):
            return True
        return False

    def check(self, context):
        from presto.declaration.CategoryDeclaration import CategoryDeclaration
        named = context.getRegistered(self.name)
        if named is None:
            raise SyntaxError("Unknown identifier:" + self.name)
        elif isinstance(named, Variable):  # local variable
            return named.getType(context)
        elif isinstance(named, LinkedVariable):  # linked variable
            return named.getType(context)
        elif isinstance(named, IArgument):  # named argument
            return named.getType(context)
        elif isinstance(named, CategoryDeclaration):  # any p with x
            return named.getType(context)
        elif isinstance(named, AttributeDeclaration):  # in category method
            return named.getType(context)
        elif isinstance(named, MethodDeclarationMap):  # global method or closure
            return MethodType(context, self.name)
        else:
            raise SyntaxError(self.name + "  is not an instance:" + type(named).__name__)


    def interpret(self, context):
        o = context.getValue(self.name)
        if isinstance(o, IExpression):
            o = o.interpret(context)
        return o

